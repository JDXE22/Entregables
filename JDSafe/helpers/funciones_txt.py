from io import open

def crear_archivo_txt(nombre_archivo, contenido):
  contenido = str(contenido)
  with open(f"{nombre_archivo}.txt", "a+") as archivo:
    archivo.write(contenido + "\n")

  print(f"¡El archivo '{nombre_archivo}.txt' ha sido creado con éxito!")

def leer_archivo_txt(nombre_archivo):
  contenido = ""
  with open(f"{nombre_archivo}.txt", "r") as archivo:
       contenido = archivo.read(archivo)
  print(contenido)
