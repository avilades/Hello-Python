# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=24010

### Python Package Manager ###

# PIP https://pypi.org
# PIP es el gestor de paquetes de Python. Permite instalar librerías creadas por otros.

# Comandos útiles de terminal (ejectuados fuera de este script):
# pip install pip (actualizar pip)
# pip --version (ver versión)

# pip install numpy
import pandas
from mypackage import arithmetics
import requests
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install pandas

# pip list (listar paquetes instalados)
# pip uninstall pandas (desinstalar paquete)
# pip show numpy (mostrar información de un paquete)

# pip install requests

# Requests es una librería muy popular para hacer peticiones HTTP (web)
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package
# Ejemplo de uso de un paquete local creado por nosotros

print(arithmetics.sum_two_values(1, 4))

