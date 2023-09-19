from fastapi import APIRouter, HTTPException
from vcenter.constants import authenticate
import requests

router = APIRouter()


@router.get('/rest/vcenter/folder')
async def get_folders():
    try:
        # Autenticación y obtención de vmware-api-session-id
        session_id = authenticate.authenticate()

        # Si la autenticación fue exitosa
        if session_id:
            result = fetch_data(session_id)
            return result
        else:
            raise HTTPException(
                status_code=401, detail="Error de autenticación")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def fetch_data(session_id):
    try:
        base_url = 'https://10.120.80.20/rest'
        url = f'{base_url}/vcenter/folder'

        headers = {'vmware-api-session-id': session_id}

        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()

        data = response.json()

        if data is None:
            raise HTTPException(
                status_code=500, detail="No se pudieron obtener los datos.")

        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
