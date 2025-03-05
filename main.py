import Servicios.azure_service as azs
import Servicios.convert_service as cs

# Se realiza la descarga del archivo
azs.download_files_blob()
cs.convert_to_json()