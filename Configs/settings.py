from pathlib import Path
from dotenv import load_dotenv
import os

root = Path.cwd().absolute()
path_env = Path(f'{root}/.env').absolute()
load_dotenv('/home/investors/ai_investors/projects/workerdown_investors/.env')

try:
    CLIENT_SECRET = os.environ['secret_client_key']
    TENANT_ID = os.environ['tenant_id']
    CLIENT_ID = os.environ['client_id']
except KeyError as e:
    print(f'La variable {e.args} no está definida')
