from fastapi import FastAPI
from vcenter import get_folders, get_networks, get_datastores
from vcenter import get_vms, create_vm
app = FastAPI()


# Obtiene VMs
app.include_router(get_vms.router)

# Obtiene folders
app.include_router(get_folders.router)

# Obtiene networks
app.include_router(get_networks.router)

# Obtiene datastores
app.include_router(get_datastores.router)

# Crear VM
app.include_router(create_vm.router)
