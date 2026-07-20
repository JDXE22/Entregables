from datetime import datetime
asistencia_y_observaciones = []
print("Bienvenido al apartado de asistencias y observaciones \n")
print("A continuacion se va a desplegar un menu que funciona con numeros \n")

def registrar_asistencia_y_observacion():
  cita = input("Ingrese el codigo de la cita")
  fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S").date()
  for asistencia in asistencia_y_observaciones.values():
      if asistencia["codigo"] == cita:
        observacion = input("Inserte la observacion de la clase")
        resultado = {f"Codigo:{cita}, Fecha:{fecha}, Observacion:{observacion}"}
        asistencia_y_observaciones.append(resultado)
        print("Asistencia y observacion registrada con exito")
        
def consultar_asistencia_y_observacion():
  cita = input("Ingrese el codigo de la cita")
  for asistencia in asistencia_y_observaciones:
          if asistencia["codigo"] == cita:
            print(asistencia_y_observaciones)

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
            
      elif opcion == 3:
        print("Saliendo del apartado de asistencias y observaciones")
        break
    
  except ValueError:
      print("Opcion invalida. Por favor, ingrese un numero valido.")
  
  except KeyError:
      print("Codigo de cita no encontrado. Por favor, ingrese un codigo valido.")
  
  except Exception as e:
      print(f"Ocurrio un error inesperado: {e}")
    
            
              
        

    



