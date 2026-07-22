from datetime import datetime
from helpers import funciones_txt as funciones

def registrar_asistencia_y_observacion():
  while True:
    try:
      cita = input("Ingrese el codigo de la cita \n")
      existe = funciones.leer_archivo_txt("asistencias")
      for asistencia in existe:
        if asistencia["codigo"] == cita:
            print("Ya existe una asistencia y observacion registrada para esta cita")
            return
      else:
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        observacion = input("Ingrese la observacion de la clase: \n" )

        
    except ValueError:
      print("El dato ingresado no es valido, por favor ingrese un dato valido \n")
    
    except TypeError as e:
      print(f"Se ha ingresado un dato no valido {e}\n")
      
    except Exception as e:
      print(f"Se ha presentado un error inesperado {e}\n")
      
    else: 
        asistencia = {"codigo": cita, "fecha": fecha, "observacion": observacion}
        funciones.crear_archivo_txt("asistencias",contenido=asistencia)
        print("Asistencia y observacion registrada correctamente")
        
            
        
def consultar_asistencia_y_observacion():
  while True:
   try:  
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
    
   except ValueError:
      print("El dato ingresado no es valido, por favor ingrese un dato valido \n")

   except TypeError as e:
      print(f"Se ha ingresado un dato no valido {e}\n")
      
   except Exception as e:
      print(f"Se ha presentado un error inesperado {e}\n")










