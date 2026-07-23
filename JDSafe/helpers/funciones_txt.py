from io import open
import ast
from helpers import funciones_txt as funciones

citas = funciones.leer_archivo_txt("citas_clientes")


def crear_archivo_txt(nombre_archivo, contenido):
  with open(f"data/{nombre_archivo}.txt", "a+") as archivo:
    archivo.write(str(contenido) + "\n")
  print(f"¡El archivo '{nombre_archivo}.txt' ha sido creado con éxito! \n")

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

citas = funciones.leer_archivo_txt("citas_clientes")

def verificar_cliente(cliente):
    clientes = funciones.leer_archivo_txt("clientes")
    for registro in clientes:
        if int(registro['documento']) == cliente:
            return True 
    else: 
        return False

def verificar_disponibilidad_instructor(instructor, fecha, hora):
    for cita in citas:
        if cita['instructor'] == instructor and cita['fecha'] == fecha and cita['hora'] == hora:
            return False
    else:
        return True

def verificar_disponibilidad_vehiculo(vehiculo, fecha, hora):
    for cita in citas:
        if cita['vehiculo'] == vehiculo and cita['fecha'] == fecha and cita['hora'] == hora:
            return False
    else:
        return True