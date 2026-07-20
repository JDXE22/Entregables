print("Bienvenido a la interfaz de citas de JDSafe\n")
print("A continuacion se va a desplegar un menu que funciona con numeros \n")
print("Si ingresa una opcion incorrecta, el menu se desplegara otra vez\n")
print("1. Programar citas ")
print("2. Consultar citas agendadas por cliente")
print("3. Consultar citas agendadas por fecha")
print("Para salir del menu, ingrese 0\n")

citas = []

def agendar_cita():
    cliente = int(input("Ingresar numero de documento de 10 digitos del cliente, sin comas o espacios. \n"))
    instructor = input("Seleccione el instructor con el que desea tener la clase")
    vehiculo = input("Seleccione el tipo de vehiculo")
    fecha = input("Ingrese en formato DD/MM/YY la fecha de la cita")
    hora = input("Ingrese en formato HH:MM la hora de la cita")
    
    cita = {
      "cliente": cliente,
      "instructor": instructor,
      "vehiculo": vehiculo,
      "fecha": fecha,
      "hora": hora
    }

    citas.append(cita)

    with open("citas.txt", "w") as archivo:
      for cita in citas:
        archivo.write(f"Cliente: {cita['cliente']}, Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}\n")

def consultar_citas_por_cliente(cliente):
   citas_cliente = []
   for cita in citas:
      if cita["cliente"] == cliente:
        print(f"Se ha encontrado los siguientes resultados del cliente: {cita["cliente"]}")
        citas_cliente.append(cita)
      return citas_cliente
    
def consultar_citas_por_instructor(instructor):
   citas_instructor = []
   for cita in citas:
      if cita["instructor"] == instructor:
        print(f"Se ha encontrado los siguientes resultados del instructor: {cita["instructor"]}")
        citas_instructor.append(cita)
      return citas_instructor


while True:
  opcion = int(input("Ingrese la opcion: \n"))
  if opcion == 1:
   agendar_cita()
  if opcion == 2:
    cliente = int(input("Ingresar numero de documento de 10 digitos del cliente, sin comas o espacios. \n"))
    consultar_citas_por_cliente(cliente)
      
  if opcion == 3:
     instructor = int(input("Ingresar numero de documento de 10 digitos del instructor, sin comas o espacios. \n"))
     consultar_citas_por_instructor(instructor)
              
           




