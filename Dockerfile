# Usa una imagen base de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Recoge archivos estáticos (como admin y Swagger UI)
RUN python manage.py collectstatic --noinput

# Expone el puerto que usará Cloud Run
EXPOSE 8080

# Ejecuta el servidor con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "ecommerce.wsgi"]
