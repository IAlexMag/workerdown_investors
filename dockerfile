# Usa una imagen base con Python 3.12
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema (Java y otras necesarias para PySpark)
RUN apt-get update && apt-get install -y openjdk-21-jdk && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Definir variable de entorno para Java (requerida por PySpark)
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Definir que se carguen las variables del .env dentro del script
# No es necesario instalar python-dotenv por separado si ya está en requirements.txt

# Comando para ejecutar el script sin depender de `source .env`
CMD ["python", "main.py"]
