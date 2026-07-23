from helpers import funciones_txt as funciones

def creacion_de_clientes():
    lista_clientes = funciones.leer_archivo_txt("clientes")

    print("Bienvenido al sistema de creación de clientes")
    print("Dentro de este formulario debe ingresar los siguientes datos:")
    print("1. Primer nombre y primer apellido")
    print("2. Número de documento")
    print("3. Seleccionar curso de aprendizaje (Moto, carro o ambos)\n")

    while True:
        nombre = input("Ingrese su primer nombre y primer apellido: \n").strip()
        sin_espacios = nombre.replace(" ", "")
        
        if sin_espacios.isalpha():
            tamano = funciones.calcular_tamaño(nombre)
            if 6 <= tamano <= 50:
                nombre = nombre.upper() 
                print(f"Nombre válido. Bienvenido/a, {nombre}\n")
                break
            else: 
                print(f"El nombre solo contiene letras, pero su longitud ({tamano}) debe estar entre 6 y 50 caracteres.")
                print("Intente de nuevo.\n")
        else:
            print("El nombre ingresado no es válido. No debe contener números ni símbolos.")
            print("Intente de nuevo.\n")

    while True:
        documento = input("Ingresar número de documento de 10 dígitos (sin espacios ni puntos): \n").strip()
        sin_espacios = documento.replace(" ", "")
        
        if sin_espacios.isdigit():
            tamano_doc = funciones.calcular_tamaño(documento)
            #6 <= tamano_doc 10:
            if tamano_doc == 10:
                existe = False
                for cliente in lista_clientes:
                    if cliente["documento"] == documento:
                        existe = True
                        break
                
                if existe:
                    print(f"Error: El documento {documento} ya se encuentra registrado a nombre de otro cliente.")
                    print("Por favor, ingrese un número de documento diferente.\n")
                    continue 
                
                print(f"Documento válido: {documento}\n")
                break
            else:
                print(f"El documento solo contiene números, pero su longitud ({tamano_doc}) no esta en el rango de 6 a 10 dígitos.")
                print("Intente de nuevo.\n")
        else:
            print("El documento ingresado no es válido. No debe contener letras ni símbolos.")
            print("Intente de nuevo.\n")

    while True:
        try:
            print("Seleccione curso de aprendizaje:")
            print("1. Moto")
            print("2. Carro")
            print("3. Ambos (Carro y Moto)")
            
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1:
                sel = "Moto"
            elif opcion == 2:
                sel = "Carro"
            elif opcion == 3:
                sel = "Ambos (Carro y Moto)"
            else:
                print("Opción no válida. Por favor ingrese 1, 2 o 3.\n")
                continue  

            print(f"\nCurso seleccionado: {sel}")
            break
                
        except ValueError as e:
            print(f"Entrada inválida. Debe ingresar un número entero: {e}\n")

    cliente_formato_txt = {
        "nombre": nombre,
        "documento": documento,
        "curso": sel
    }
    funciones.crear_archivo_txt("clientes", cliente_formato_txt)

    print("\nLista actualizada de clientes:")
    lista_actualizada = funciones.leer_archivo_txt("clientes")
    for cliente in lista_actualizada:
        print(f"Nombre: {cliente['nombre']}, Documento: {cliente['documento']}, Curso: {cliente['curso']}")