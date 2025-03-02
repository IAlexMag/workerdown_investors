import Services.azure_service as azs
import Services.convert_service as cs

# Se realiza la descarga del archivo
azs.download_files_blob()
cs.convert_to_json()