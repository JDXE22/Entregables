from datetime import datetime
from helpers import funciones_txt as funciones

citas = funciones.leer_archivo_txt("citas_clientes")

def agendar_cita():
  while True:
    try:
      cliente = int(input("Ingresar numero de documento de 10 digitos del cliente, sin comas o espacios. \n"))
      instructor = input("Seleccione el instructor con el que desea tener la clase \n")
      vehiculo = input("Seleccione el tipo de vehiculo: 1. Moto 2. Carro \n")
      if vehiculo == "1":
          vehiculo = "Moto"
      elif vehiculo == "2": 
          vehiculo = "Carro"
      else: 
          print("Opcion de vehiculo no valida, por favor ingrese una opcion valida")
          return
      fecha_insertada = input("Ingrese en formato DD/MM/YY la fecha de la cita \n")
      hora_insertada = input("Ingrese en formato HH:MM la hora de la cita \n")
      fecha_f = datetime.strptime(fecha_insertada, "%d/%m/%y").strftime("%d/%m/%y")
      hora_f = datetime.strptime(hora_insertada, "%H:%M").strftime("%H:%M")
      
      cita = {
        "cliente": cliente,
        "instructor": instructor,
        "vehiculo": vehiculo,
        "fecha": fecha_f,
        "hora": hora_f
      }      
      funciones.crear_archivo_txt("citas_clientes", cita)
      print("Cita agendada correctamente")
      return

    except ValueError:
      print("El dato ingresado no es valido, por favor ingrese un dato valido \n")
      
    except TypeError as e:
      print(f"Se ha ingresado un dato no valido {e}\n")
      
    except Exception as e:
      print(f"Se ha presentado un error inesperado {e}\n")
    
def consultar_citas_por_cliente():
  try:
    cliente = int(input("Ingresar numero de documento de 10 digitos del cliente, sin comas o espacios. \n"))
    for cita in citas:
        if cita['cliente'] == cliente:
          print(f"Se ha encontrado los siguientes resultados del cliente: {cita['cliente']}")
          print(f"Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Fecha: {cita['fecha']}, Hora: {cita['hora']} \n")
          return
  
  except ValueError:
    print("El documento ingresado no es valido, por favor ingrese un numero de documento valido \n")
  except Exception as e:
    print(f"Se ha presentado un error inesperado {e}\n")
    
def consultar_citas_por_fecha():
  try:
    fecha = input("Ingresar la fecha de la cita programada \n")
    fecha_f = datetime.strptime(fecha, "%d/%m/%y").strftime("%d/%m/%y")
    for cita in citas:
        if cita['fecha'] == fecha_f:
          print(f"Se ha encontrado los siguientes resultados de la fecha: {cita['fecha']} \n")
          print(f"Cliente: {cita['cliente']}, Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Hora: {cita['hora']} \n")
          return
          
  except ValueError:
    print("El formato de la fecha ingresada no es valido, por favor ingrese la fecha en el formato DD/MM/YY \n")
    
  except Exception as e:
    print(f"Se ha presentado un error inesperado {e}\n")




