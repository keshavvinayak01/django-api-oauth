import requests
import json
from global_config import get_global_config

def get_jwt_details():
    active_config = get_global_config()
    r = requests.post('http://127.0.0.1:8000/api/token',
                    json={
                        'username' : active_config['superuser']['username'],
                        'password' : active_config['superuser']['password']
                    }).json()
    return(r)

print(get_jwt_details())