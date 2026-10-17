# API de Chat Inteligente con Historial y Persistencia (FastAPI + SQLAlchemy + Docker)

Microservicio backend avanzado desarrollado con **FastAPI** y una arquitectura modular limpia, diseñado para procesar lenguaje natural mediante la API de Groq y almacenar de forma persistente todas las interacciones en una base de datos local utilizando **SQLite y SQLAlchemy**.

---

## Tecnologías y Arquitectura

* **Python 3.11**
* **FastAPI** (Framework asíncrono de alto rendimiento)
* **SQLAlchemy** (ORM para la gestión de bases de datos relacionales)
* **SQLite** (Base de datos local ligera y embebida)
* **OpenAI SDK & Groq API** (Inferencia de modelos LLM optimizados)
* **Docker** (Contenerización completa del servicio)

---

## Estructura del Proyecto (Patrón Modular)

```text
ia-chat-backend/
│
├── app/
│   ├── __init__.py
│   ├── database.py       # Configuración del motor y sesión de SQLAlchemy
│   ├── models.py         # Definición de modelos de la base de datos (Tablas)
│   ├── schemas.py        # Esquemas de validación de datos con Pydantic
│   ├── crud.py           # Operaciones de persistencia (Create/Read)
│   ├── services.py       # Capa de integración y llamadas a la API de IA
│   └── main.py           # Inicialización de FastAPI y registro de rutas
│
├── .env                  # Variables de entorno (Credenciales de API)
├── Dockerfile            # Instrucciones de empaquetado Docker
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación técnica


Requisitos Previos
Tener instalado Docker Desktop y asegurarte de que está en ejecución.

Disponer de una clave de API activa de Groq Console.


Guía de Instalación y Despliegue con Docker
1. Crea un archivo .env en la raíz del proyecto añadiendo tu clave de acceso:
GROQ_API_KEY=tu_clave_real_de_groq

2. Construye la imagen Docker del microservicio:
docker build -t ia-chat-backend .

3. Ejecuta el contenedor exponiendo el puerto 8000:
docker run --name ia-chat-backend --env-file .env -p 8000:8000 ia-chat-backend


Documentación Interactiva y Endpoints
Una vez que el contenedor esté en marcha, accede a la documentación interactiva generada automáticamente en:
   http://localhost:8000/docs


1. Enviar mensaje a la IA (POST /chat)
Envía un prompt al modelo, el cual procesa la respuesta, la devuelve al cliente y la almacena automáticamente de forma persistente en la base de datos SQLite.

Cuerpo de la petición (JSON):
{
  "prompt": "¿Cuáles son las ventajas de usar SQLAlchemy?"
}

Respuesta exitosa (200 OK):
{
  "id": 1,
  "prompt": "¿Cuáles son las ventajas de usar SQLAlchemy?",
  "response": "SQLAlchemy proporciona un ORM potente...",
  "created_at": "2026-09-23T20:20:41.126459"
}



2. Consultar historial (GET /history)
Recupera el listado completo de interacciones pasadas ordenadas cronológicamente de la más reciente a la más antigua, con soporte para paginación (skip y limit).
