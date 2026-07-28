from io import open
import ast

def crear_archivo_txt(nombre_archivo, contenido):
  try:
    with open(f"data/{nombre_archivo}.txt", "a+", encoding="utf-8") as archivo:
      archivo.write(str(contenido) + "\n")
    print(f"¡El archivo '{nombre_archivo}.txt' ha sido creado/actualizado con éxito! \n")
    return True
  except IOError as e:
    print(f"Error de E/S al crear o escribir en '{nombre_archivo}.txt': {e}")
    return False
  except Exception as e:
    print(f"Error inesperado al crear el archivo '{nombre_archivo}.txt': {e}")
    return False
  
def actualizar_archivo_txt(nombre_archivo, registros):
  try:
    with open(f"data/{nombre_archivo}.txt", "w", encoding="utf-8") as archivo:
      for linea in registros:
        archivo.write(str(linea) + "\n")
    return True
  except IOError as e:
    print(f"Error de E/S al actualizar el archivo '{nombre_archivo}.txt': {e}")
    return False
  except Exception as e:
    print(f"Error inesperado al actualizar el archivo '{nombre_archivo}.txt': {e}")
    return False

def leer_archivo_txt(nombre_archivo):
  try:
    registros = []
    with open(f"data/{nombre_archivo}.txt", "r", encoding="utf-8") as archivo:
      for linea in archivo: 
        linea = linea.strip()
        if linea:
          try:
            registros.append(ast.literal_eval(linea))
          except (ValueError, SyntaxError) as e:
             print(f"Registro con formato inválido en '{nombre_archivo}.txt' omitido. Error: {e}")
             pass
    print(f"Se han leído {len(registros)} registros del archivo '{nombre_archivo}.txt'.")
    return registros
  except FileNotFoundError:
    return []
  except IOError as e:
    print(f"Error de E/S al leer el archivo '{nombre_archivo}.txt': {e}")
    return []
  except Exception as e:
    print(f"Error inesperado al leer el archivo '{nombre_archivo}.txt': {e}")
    return []

def calcular_tamaño(name):
  try:
    sin_espacios = name.replace(" ", "")
    tamaño = len(sin_espacios)
    return tamaño
  except Exception as e:
    print(f"Error al calcular el tamaño: {e}")
    return 0
