from io import open
import ast

def crear_archivo_txt(nombre_archivo, contenido):
  with open(f"/data{nombre_archivo}.txt", "a+") as archivo:
    archivo.write(str(contenido) + "\n")
  print(f"¡El archivo '{nombre_archivo}.txt' ha sido creado con éxito!")

def leer_archivo_txt(nombre_archivo):
  try:
    registros = []
    with open(f"data/{nombre_archivo}.txt", "r") as archivo:
      for linea in archivo: 
        linea = linea.strip()
        if linea:
          registros.append(ast.literal_eval(linea))
  except FileNotFoundError:
      print(f"El archivo '{nombre_archivo}.txt' no existe aun.")
      return []
  else:
   print(f"Se han leido {len(registros)} registros del archivo '{nombre_archivo}.txt'.")
  return registros

def calcular_tamaño(name):
    sin_espacios=name.replace(" ","")
    tamaño=len(sin_espacios)
    return tamaño
