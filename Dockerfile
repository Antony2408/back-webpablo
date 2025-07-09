# Usa una imagen oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto 8080 (Cloud Run escucha en este puerto)
EXPOSE 8080

# Comando para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

