from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from pathlib import Path
from Configs.settings import CLIENT_SECRET, TENANT_ID, CLIENT_ID
import os

account_url = "https://storageinvestorsai.blob.core.windows.net"
container_name = 'datalakeenterpiseaiinvestors'
destiny_container = 'warehouseaiinvestors'
tenant_id = TENANT_ID # id del inquilino
client_id = CLIENT_ID
client_secret = CLIENT_SECRET
root = Path.cwd()
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
blob_service_client = BlobServiceClient(account_url, credential=credential)

def download_files_blob():
    try:
        container_client = blob_service_client.get_container_client(container=container_name)
        blobs = container_client.list_blobs(name_starts_with='test/')
        for blob in blobs:
            blob_client = container_client.get_blob_client(blob.name)
            download_path = Path(f'{root}/files').absolute()
            local_file_path = os.path.join(download_path, blob.name)
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            with open(local_file_path, 'wb') as download_file:
                download_file.write(blob_client.download_blob().readall())
            print(f'Blob descargado: {blob.name}')
    except Exception as e:
        print(e)

def load_json_blobs(partition):
    try:
        container_client = blob_service_client.get_container_client(container=destiny_container)
        for row in partition:
            blob_name = f'20250302/record_{row.id}.json'
            blob_client = container_client.get_blob_client(blob_name)
            blob_client.upload_blob(row.json.encode('utf-8'), overwrite = True)
    except Exception as e:
        print(e)
