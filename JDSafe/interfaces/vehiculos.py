from helpers import funciones_txt as funciones

def agregar_vehiculo():
    lista_vehiculos = funciones.leer_archivo_txt("vehiculos")

    print("Bienvenido al sistema de agregado de vehiculos")
    print("Dentro de este formulario debe de ingresar los siguientes datos")
    print("1. Seleccionar tipo de vehiculo (Moto o Carro) \n")
    print("2. Ingresar placa de el vehiculo\n")

    while True:
        try:
            print("Seleccione tipo de vehiculo")
            print("1. Moto")
            print("2. Carro")
            opcion = int(input("Ingrese una opción: \n"))
            
            if opcion == 1:
                print("El vehiculo es Moto")
                sel = "Moto"
            elif opcion == 2:
                print("El vehiculo es Carro")
                sel = "Carro"
            else:
                print("Opción no válida. Por favor ingrese 1 o 2.\n")
                continue

            print(f"\nEl vehiculo seleccionado para aprender fue {sel}")
            break 

        except ValueError as e:
            print(f"El dato ingresado no es valido: {e}\n")

    while True:
        placa = input(f"Ingrese la placa para {sel} sin espacios ni guiones: \n").replace(" ", "").upper()
        
        if len(placa) != 6:
            print(f"La placa debe tener un tamaño de 6 caracteres. No es válida: {placa} (ej. ABC123 o ABC12D).\n")
            continue

        letras_placa = placa[0:3]
        if not letras_placa.isalpha(): 
            print("Los primeros 3 caracteres deben ser letras.\n")
            continue
        
        validacion = False
        
        if sel == "Carro":
            numeros = placa[3:6]
            if numeros.isdigit():
                validacion = True
            else:
                print("Error: Los últimos 3 caracteres para un carro deben ser números (ej. ABC123).\n")
                continue
                
        elif sel == "Moto":
            numeros = placa[3:5]
            letra_final = placa[5]
            if numeros.isdigit() and letra_final.isalpha():
                validacion = True
            else:
                print("Error: La placa de moto debe tener 2 números y terminar en una letra (ej. ABC12D).\n")
                continue

        if validacion:
            existe = False
            for v in lista_vehiculos:
                if v["placa"] == placa:
                    existe = True
                    break
                    
            if existe:
                print(f"Alerta: La placa {placa} ya existe en el sistema. Ingrese una diferente.\n")
                continue  
            else:
                print(f"Placa de {sel} válida y disponible: {placa}")
                break

    nuevo_vehiculo = {
        "tipo": sel,
        "placa": placa,
        "disponible": True
    }

    funciones.crear_archivo_txt("vehiculos", nuevo_vehiculo)

    print("\nLista actualizada de vehículos:")
    lista_actualizada = funciones.leer_archivo_txt("vehiculos")
    for vehiculo in lista_actualizada:
        print(f"Tipo: {vehiculo['tipo']}, Placa: {vehiculo['placa']}, Disponible: {vehiculo['disponible']}")
    return