

FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor en /app
WORKDIR /app


#Copia todos los archivos del directorio actual en el host al directorio de trabajo del contenedor
COPY . .

RUN pip install --no-cache-dir -r requirements.txt


#Expone el puerto 8080, que será usado por la aplicación dentro del contenedor
EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
