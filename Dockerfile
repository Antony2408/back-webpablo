# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia todo el proyecto
COPY . .

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto que usará Cloud Run
EXPOSE 8080

# Comando para ejecutar el servidor con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "back_webpablo.wsgi"]

