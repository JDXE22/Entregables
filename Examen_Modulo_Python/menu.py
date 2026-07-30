print("\nBienvenido al programa DriveSafe \n")
print("A continuación se va a desplegar un menú que funciona con números. \n")
print("Si ingresa una opción incorrecta, el menú se desplegará otra vez.\n")

while True:
        print("\n--- Menú Principal ---\n")
        print("1. Registrar evaluaciones de las practicas")
        print("2. Consultar evaluaciones de las practicas por cliente") 
        print("3. Calcular de promedio general")
        print("0. Ingrese 0 para salir\n")

    opcion = int(input("Ingrese la opcion para continuar \n"))

    except ValueError:
        print("\nSe ha ingresado una opción no válida. Por favor ingrese un número entero.\n")
        continue
    except TypeError as e:
        print(f"\nSe ha ingresado una opción no válida: {e}\n")
    except Exception as err: 
        print(f"\nSe ha presentado un error inesperado: {err}\n")
    
    else:
    if opcion ==  1:
        print("Registrando evaluaciones de las practicas")
    elif opcion == 2:
        print("Consultando evaluaciones de las practicas por cliente")
    elif opcion == 3:
        print("Calculando de promedio general")
    elif opcion == 0:
        print("\nSaliendo del programa, vuelva pronto... \n")
        break
