# Imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 (Cloud Run usa este puerto)
EXPOSE 8080

# Comando para correr la app con gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
