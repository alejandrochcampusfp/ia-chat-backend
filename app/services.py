import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Inicializamos el cliente de OpenAI apuntando a la URL de Groq
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

def get_ai_response(prompt: str) -> str:
    """Envía un prompt a la IA y devuelve la respuesta generada."""
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "Eres un asistente técnico experto, claro y directo."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error al conectar con la IA: {str(e)}")