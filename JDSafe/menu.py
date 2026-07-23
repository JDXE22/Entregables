from interfaces.citas import agendar_cita, consultar_citas_por_cliente, consultar_citas_por_fecha
from interfaces.vehiculos import agregar_vehiculo
from interfaces.instructores import creacion_instructores
from interfaces.clientes import creacion_de_clientes
from interfaces.asistencias import menu_asistencias
from interfaces.horarios import mostrar_horarios_disponibles

print("\nBienvenido al programa JDSafe \n")
print("A continuación se va a desplegar un menú que funciona con números. \n")
print("Si ingresa una opción incorrecta, el menú se desplegará otra vez.\n")

while True: 
    try:
        print("\n--- Menú Principal ---\n")
        print("1. Programar citas")
        print("2. Asistencias y observaciones")
        print("3. Registrar clientes")
        print("4. Registrar instructor")
        print("5. Registrar vehículo")
        print("6. Consultar citas agendadas por fecha [formato dd/mm/aa]")
        print("7. Consultar historial del cliente")
        print("8. Consultar horarios disponibles")
        print("0. Ingrese 0 para salir\n")
        opcion = int(input("Ingrese la opción: \n"))    
        
    except ValueError:
        print("\nSe ha ingresado una opción no válida. Por favor ingrese un número entero.\n")
    except TypeError as e:
        print(f"\nSe ha ingresado una opción no válida: {e}\n")
    except Exception as err: 
        print(f"\nSe ha presentado un error inesperado: {err}\n")

    else:
        if opcion == 1: 
            agendar_cita()
        elif opcion == 2:
            menu_asistencias()
        elif opcion == 3:
            creacion_de_clientes()
        elif opcion == 4:
            creacion_instructores()
        elif opcion == 5:
            agregar_vehiculo()
        elif opcion == 6:
            consultar_citas_por_fecha()
        elif opcion == 7:
            consultar_citas_por_cliente()
        elif opcion == 8:
            mostrar_horarios_disponibles()
        elif opcion == 0:
            print("\nSaliendo del programa, vuelva pronto... \n")
            break