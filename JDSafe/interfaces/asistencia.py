from datetime import datetime
from ..helpers import funciones_txt as funciones

asistencia_y_observaciones = []
print("Bienvenido al apartado de asistencias y observaciones \n")
print("A continuacion se va a desplegar un menu que funciona con numeros \n")

def registrar_asistencia_y_observacion():
  cita = input("Ingrese el codigo de la cita \n")
  existe = funciones.leer_archivo_txt("asistencias")
  for asistencia in existe:
    if asistencia["codigo"] == cita:
        print("Ya existe una asistencia y observacion registrada para esta cita")
        return
  else:
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    observacion = input("Ingrese la observacion de la clase: \n" )
    asistencia = {"codigo": cita, "fecha": fecha, "observacion": observacion}
    asistencia_y_observaciones.append(asistencia)
    funciones.crear_archivo_txt("asistencias",contenido=asistencia)
    print("Asistencia y observacion registrada correctamente")
            
        
def consultar_asistencia_y_observacion():
  cita = input("Ingrese el codigo de la cita")
  existe = funciones.leer_archivo_txt("asistencias")
  if existe:
    for asistencia in existe:
      if asistencia["codigo"] == cita:
        print(f"Codigo de cita: {asistencia['codigo']}")
        print(f"Fecha: {asistencia['fecha']}")
        print(f"Observacion: {asistencia['observacion']}")
        return
      else:
        print("No se encontro una asistencia y observacion registrada para esta cita")
      

while True:
  try:
      print("1. Registrar asistencia y observacion")
      print("2. Consultar asistencia y observacion")
      print("Ingrese 0 para salir del apartado de asistencias y observaciones. Esto lo llevara al menu principal \n")

      opcion = int(input("Ingrese la opcion: \n"))
      
      if opcion == 1:
        registrar_asistencia_y_observacion()
      
      elif opcion == 2:
        consultar_asistencia_y_observacion()
            
      elif opcion == 0:
        print("Saliendo del apartado de asistencias y observaciones")
        break
    
  except ValueError:
      print("Opcion invalida. Por favor, ingrese un numero valido.")
  
  except KeyError:
      print("Codigo de cita no encontrado. Por favor, ingrese un codigo valido.")
      
  except FileNotFoundError:
      print("No se encontraron asistencias y observaciones registradas. Por favor, registre una asistencia y observacion primero.") 
  
  except Exception as e:
      print(f"Ocurrio un error inesperado: {e}")