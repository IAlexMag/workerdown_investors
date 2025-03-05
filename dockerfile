# Usa una imagen base con Java y Debian
FROM openjdk:21-jdk-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para Spark y Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    tar \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Crear un entorno virtual y asegurarse de que tenga pip
RUN python3 -m venv /app/venv && /app/venv/bin/python -m ensurepip

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar dependencias de Python en el entorno virtual
RUN /app/venv/bin/python -m pip install --no-cache-dir -r requirements.txt

# Descargar y extraer Spark
# Ajusta la versión de Spark según tus necesidades
ARG SPARK_VERSION=3.5.5
ARG HADOOP_VERSION=3
RUN wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Establecer variables de entorno de Spark
ENV SPARK_HOME /opt/spark
ENV PATH $SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON /app/venv/bin/python

# Definir el comando de ejecución usando el entorno virtual y Spark
CMD ["spark-submit", "main.py"]