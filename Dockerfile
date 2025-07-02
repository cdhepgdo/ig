FROM python:3.11-slim

# Instala dependencias del sistema (opcional pero recomendado)
RUN apt-get update && apt-get install -y curl ffmpeg && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará gunicorn
EXPOSE 5000

# Comando para lanzar la app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
