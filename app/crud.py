from sqlalchemy.orm import Session
from app.models import MessageModel

def create_message(db: Session, prompt: str, response: str):
    """Guarda una nueva interacción (prompt y respuesta) en la base de datos."""
    db_message = MessageModel(prompt=prompt, response=response)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    """Recupera el historial de mensajes ordenados del más reciente al más antiguo."""
    return db.query(MessageModel).order_by(MessageModel.created_at.desc()).offset(skip).limit(limit).all()