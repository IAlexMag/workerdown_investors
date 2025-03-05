from dotenv import load_dotenv
import os

load_dotenv()

try:
    CLIENT_SECRET = os.environ['secret_client_key']
    TENANT_ID = os.environ['tenant_id']
    CLIENT_ID = os.environ['client_id']
except KeyError as e:
    print(f'La variable {e.args} no está definida')
