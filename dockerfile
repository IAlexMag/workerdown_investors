# Usa una imagen base con Java y Debian
FROM openjdk:21-jdk-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar Python y herramientas necesarias
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Crear un entorno virtual y activarlo
RUN python3 -m venv /app/venv

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar dependencias en el entorno virtual
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Definir el comando de ejecución usando el entorno virtual
CMD ["/app/venv/bin/python", "main.py"]
