# vCenter - App

## Instrucciones de instalación

## Instalar componentes desde los repositorios de Ubuntu

sudo apt update

sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

sudo apt install python3-venv

## Clonar repositorio

git clone <https://github.com/mmunarriz/vcenter_app.git>

## Crear entorno virtual e instalar componentes de FastAPI

~$ cd vcenter_app/

~/vcenter_app$ python3 -m venv env

~/vcenter_app$ source env/bin/activate

(env) ~/vcenter_app$ python -m pip install --upgrade pip

(env) ~/vcenter_app$ pip install "fastapi[all]"

## Instrucciones de ejecución

~$ cd vcenter_app/

~/vcenter_app$ source env/bin/activate

(env) ~/vcenter_app$ cd aplicacion

(env) ~/vcenter_app/aplicacion$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## Ejemplos de uso

Obtener VMs:
GET <http://127.0.0.1:8000/rest/vcenter/vm>

Obtener Folders:
GET <http://127.0.0.1:8000/rest/vcenter/folder>

Obtener Networks:
GET <http://127.0.0.1:8000/rest/vcenter/network>

Obtener Datastores:
GET <http://127.0.0.1:8000/rest/vcenter/datastore>

Crear VM:
POST <http://127.0.0.1:8000/rest/vcenter/create_vm>

    Body:
        {
            "vm_name": "123test_api"
        }
