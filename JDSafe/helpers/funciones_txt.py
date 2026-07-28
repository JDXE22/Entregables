from io import open
import ast
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

def obtener_ruta_archivo(nombre_archivo):
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, f"{nombre_archivo}.txt")

def crear_archivo_txt(nombre_archivo, contenido):
  ruta = obtener_ruta_archivo(nombre_archivo)
  with open(ruta, "a+", encoding="utf-8") as archivo:
    archivo.write(str(contenido) + "\n")
  print(f"¡El archivo '{nombre_archivo}.txt' ha sido creado/actualizado con éxito! \n")
  
def actualizar_archivo_txt(nombre_archivo, registros):
  try:
    ruta = obtener_ruta_archivo(nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as archivo:
      for linea in registros:
        archivo.write(str(linea) + "\n")
  except IOError:
      print(f"Error al actualizar el archivo '{nombre_archivo}.txt'.")
      return False

def leer_archivo_txt(nombre_archivo):
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
      print(f"Error al leer el archivo '{nombre_archivo}.txt'.")
      return []
  else:
    print(f"Se han leído {len(registros)} registros del archivo '{nombre_archivo}.txt'.")
  return registros

def calcular_tamaño(name):
    sin_espacios = name.replace(" ", "")
    tamaño = len(sin_espacios)
    return tamaño
