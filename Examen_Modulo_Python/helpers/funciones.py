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
  try:
    registros = []
    ruta = obtener_ruta_archivo(nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as archivo:
      for linea in archivo: 
        linea = linea.strip()
        if linea:
          try:
            registros.append(ast.literal_eval(linea))
          except (ValueError, SyntaxError):
            pass
  except FileNotFoundError:
      return []
  except IOError:
      print(f"Error al leer el archivo '{nombre_archivo}.json'.")
      return []
  else:
    print(f"Se han leído {len(registros)} registros del archivo '{nombre_archivo}.json'.")
  return registros

def calcular_tamaño(name):
  sin_espacios = name.replace(" ", "")
  tamaño = len(sin_espacios)
  return tamaño