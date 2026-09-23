from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app import schemas, crud, services

# Crea las tablas en la base de datos SQLite automáticamente al arrancar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Chat Inteligente con Historial",
    description="Microservicio avanzado con FastAPI, SQLAlchemy y Groq IA.",
    version="2.0.0"
)

@app.post("/chat", response_model=schemas.ChatResponse)
def chat_with_ai(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    """Envía un prompt a la IA, obtiene la respuesta y la guarda en la base de datos."""
    try:
        # 1. Obtener la respuesta de la IA a través del servicio
        ai_response = services.get_ai_response(request.prompt)
        
        # 2. Guardar en la base de datos SQLite
        saved_message = crud.create_message(db=db, prompt=request.prompt, response=ai_response)
        
        return saved_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history", response_model=list[schemas.ChatResponse])
def get_chat_history(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtiene el historial de conversaciones guardadas en la base de datos."""
    messages = crud.get_messages(db=db, skip=skip, limit=limit)
    return messages