# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código fuente de la API al contenedor
COPY API_Interacciones /app/API_Interacciones
COPY interacciones.db /app/

# Instala las dependencias necesarias
RUN pip install fastapi pydantic requests sqlalchemy typing uvicorn

# Comando para ejecutar la aplicación
CMD ["uvicorn", "API_Interacciones.main:app", "--host", "0.0.0.0", "--port", "8002"]
