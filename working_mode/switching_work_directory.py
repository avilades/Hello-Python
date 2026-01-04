import os

# 1. Obtener la ruta del directorio donde está el script
directorio_script = os.path.dirname(os.path.abspath(__file__))

# 2. (Opcional) Cambiar el directorio de trabajo actual
os.chdir(directorio_script)

# 3. Referenciar archivos de forma relativa
#ruta_archivo_datos = os.path.join("datos.csv")

print(f"Directorio de trabajo actual: {os.getcwd()}")
# print(f"Ruta del archivo de datos: {os.path.abspath(ruta_archivo_datos)}") # Para la ruta absoluta
