from io import open
import ast
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

def obtener_ruta_archivo(nombre_archivo):
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, f"{nombre_archivo}.json")

def crear_archivo(nombre_archivo, contenido):
  ruta = obtener_ruta_archivo(nombre_archivo)
  with open(ruta, "a+", encoding="utf-8") as archivo:
    json.dump(contenido, archivo, indent=2)
  print(f"¡El archivo '{nombre_archivo}.json' ha sido creado/actualizado con éxito! \n")

def leer_archivo(nombre_archivo):
    ruta = obtener_ruta_archivo(nombre_archivo)
    if not os.path.exists(ruta):
        print(f"El archivo '{nombre_archivo}.json' no existe.")
        return []
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        if contenido.strip() == "":
            return []
        try:
            data = json.loads(contenido)
            if isinstance(data, dict):
                return [data]
            return data
        except json.JSONDecodeError:
            print(f"Error: El archivo '{nombre_archivo}.json' no contiene un JSON válido.")
            return []

def calcular_tamaño(name):
  sin_espacios = name.replace(" ", "")
  tamaño = len(sin_espacios)
  return tamaño