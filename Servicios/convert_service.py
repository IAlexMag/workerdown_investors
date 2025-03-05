import os
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_json, struct, monotonically_increasing_id
from Servicios.azure_service import load_json_blobs

def convert_to_json():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        servicios_dir = os.path.join(script_dir, "Servicios")
        # Se realiza la descarga del archivo
        spark = SparkSession.builder.appName("convert_session").getOrCreate()
        spark.sparkContext.addPyFile(os.path.join(servicios_dir, "__init__.py"))
        spark.sparkContext.addPyFile(os.path.join(servicios_dir, "azure_services.py"))
        spark.sparkContext.addPyFile(os.path.join(servicios_dir, "convert_service.py"))
        root = Path.cwd()
        folder_path = Path(f'{root}/files/test/').absolute()
        for file in os.listdir(folder_path):
            if file.endswith('.csv'):
                file_path = Path(f'{folder_path}/{file}').absolute()
                df = spark.read.csv(str(file_path), header= True, inferSchema=True)
                df = df.withColumn('id', monotonically_increasing_id())
                df.select(to_json(struct(*df.columns)).alias("json"),"id").rdd.mapPartitions(load_json_blobs).count()
                print("Todos los registros guardados como blobs")
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        spark.stop()