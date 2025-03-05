FROM openjdk:21-jdk-slim

WORKDIR /app

# Instalar Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Comando para ejecutar el script
CMD ["python3", "main.py"]
