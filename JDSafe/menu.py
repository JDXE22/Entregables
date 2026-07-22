from interfaces.citas import agendar_cita, consultar_citas_por_cliente, consultar_citas_por_fecha 
print("Bienvenido al programa JDSafe \n")
print("A continuacion se va a desplegar un menu que funciona con numeros \n")
print("Si ingresa una opcion incorrecta, el menu se desplegara otra vez\n")

while True: 
    try:
        print("1. Programar citas ")
        print("2. Asistencias y observaciones ")
        print("3. Registrar clientes")
        print("4. Registrar instructor")
        print("5. Registrar vehiculo")
        print("6. Consultar citas agendadas")
        print("7. Consultar historial del cliente")
        print("Ingrese 0 para terminar las votaciones y ver los resultados finales")
        opcion = int(input("Ingrese la opcion: \n"))    
        
    except TypeError as e:
        print("Se ha ingresado una opcion no valido\n")
    except Exception as err: 
        print(f"Se ha presentado un error inesperado {err}\n")

    else:
        if opcion == 1: 
            agendar_cita()
        elif opcion == 2:
            print("Registro de asistencia y observaciones \n")
        elif opcion == 3:
            print("Registro de cliente \n")
        elif opcion == 4:
                print("Registro de instructor \n")
        elif opcion == 5:
                print("Registro de vehiculos \n")
        elif opcion == 6:
                print("Consultar citas \n")
        elif opcion == 7:
                consultar_citas_por_cliente()
        elif opcion == 0:
            print("Saliendo de el programa, vuelva pronto... \n")
            break


