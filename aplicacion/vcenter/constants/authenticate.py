import requests
from fastapi import HTTPException

def authenticate():
    try:
        url = "https://10.120.80.20/rest/com/vmware/cis/session"
        headers = {
            'Authorization': 'Basic YWRtaW5pc3RyYXRvckB2c3BoZXJlLmxvY2FsOkYxYjNyYzBycCE=',
            'Cookie': 'vmware-api-session-id=f259ceefc327565b6ca2ecb25ba6c465'
        }

        response = requests.post(url, headers=headers, verify=False)
        response.raise_for_status()

        session_id = response.json().get('value')

        if session_id is None:
            raise HTTPException(status_code=401, detail="No se pudo obtener el vmware-api-session-id")

        return session_id
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
