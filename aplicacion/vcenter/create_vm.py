from fastapi import APIRouter, HTTPException, Request
from vcenter.constants import authenticate
import requests

router = APIRouter()


@router.post('/rest/vcenter/create_vm')
async def create_vm(request: Request):
    try:
        req_data = await request.json()
        if 'vm_name' not in req_data:
            error = "Faltan datos"
            raise Exception(error)

        vm_name = req_data['vm_name']

        # Autenticación y obtención de vmware-api-session-id
        session_id = authenticate.authenticate()

        # Si la autenticación fue exitosa
        if session_id:
            result = fetch_data(session_id, vm_name)
            return result
        else:
            raise HTTPException(
                status_code=401, detail="Error de autenticación")
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


def fetch_data(session_id, vm_name):
    try:
        base_url = 'https://10.120.80.20/rest'
        url = f'{base_url}/vcenter/vm-template/library-items/1bdc89b9-e7ed-454e-87f5-c09f94434a64?action=deploy'

        headers = {'vmware-api-session-id': session_id}

        payload = {
            "spec": {
                "name": vm_name,
                "placement": {
                    "folder": "group-v6863",
                    "resource_pool": "resgroup-85"
                },
                "powered_on": False
            }
        }

        response = requests.post(url, headers=headers,
                                 json=payload, verify=False)
        response.raise_for_status()

        data = response.json()

        if data is None:
            raise HTTPException(
                status_code=500, detail="No se pudieron obtener los datos.")

        return data
    except requests.exceptions.RequestException as error:
        raise HTTPException(status_code=500, detail=str(error))
