from helpers import funciones_txt as funciones
lista_instructores = funciones.leer_archivo_txt("instructores")
def creacion_instructores():

    print("Bienvenido al sistema de creacion de instructores")
    print("Dentro de este formulario debe ingresar los siguientes datos:")
    print("1. Primer nombre y primer apellido")
    print("2. Numero de documento")
    print("3. Seleccionar especialidad de enseñanza (Moto, carro o ambos)\n")

    while True:
        nombre = input("Ingrese su primer nombre y primer apellido: \n").strip()
        sin_espacios = nombre.replace(" ", "")
        
        if sin_espacios.isalpha():
            tamano = funciones.calcular_tamaño(nombre)
            if 6 <= tamano <= 50:
                nombre = nombre.upper()  
                print(f"Nombre válido. Bienvenido, instructor {nombre}\n")
                break
            else: 
                print(f"El nombre solo contiene letras, pero su longitud ({tamano}) debe estar entre 6 y 50 caracteres.")
                print("Intente de nuevo.\n")
        else:
            print("El nombre ingresado no es válido. No debe contener números ni símbolos.")
            print("Intente de nuevo.\n")

    while True:
        documento = input("Ingresar numero de documento de 10 dígitos (sin espacios ni puntos): \n").strip()
        sin_espacios = documento.replace(" ", "")
        
        if sin_espacios.isdigit():
            tamano_doc = funciones.calcular_tamaño(documento)
            
            if tamano_doc == 10:
                existe = False
                for inst in lista_instructores:
                    if inst["documento"] == documento:
                        existe = True
                        break
                
                if existe:
                    print(f"El documento {documento} ya se encuentra registrado. Ingrese uno diferente.\n")
                    continue
                
                print(f"Documento válido: {documento}\n")
                break
            else:
                print(f"El documento solo contiene números, pero su longitud ({tamano_doc}) no es de 10 dígitos.")
                print("Intente de nuevo.\n")
        else:
            print("El documento ingresado no es válido. No debe contener letras ni símbolos.")
            print("Intente de nuevo.\n")

    while True:
        try:
            print("Seleccione especialidad de enseñanza:")
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

            print(f"\nEspecialidad seleccionada: {sel}")
                
        except ValueError as e:
            print(f"Entrada inválida. Debe ingresar un número entero: {e}\n")

        nuevo_instructor = {
            "nombre": nombre,
            "documento": documento,
            "especialidad": sel,
            "disponible": True 
        }

        lista_instructores.append(nuevo_instructor)

        instructor_Nuevo = (
            "Registro de Instructor Nuevo \n"
            f"Nombre: {nombre} \n"
            f"Documento: {documento} \n"
            f"Especialidad: {sel} \n"
            f"Disponibilidad: {nuevo_instructor['disponible']} \n"
            "---------------------------------------\n"
        )

        funciones.crear_archivo_txt("instructores", instructor_Nuevo)

        print("\nLista actualizada de instructores:")
        for instructor in lista_instructores:
            print(f"Nombre: {instructor['nombre']}, Documento: {instructor['documento']}, Especialidad: {instructor['especialidad']}, Disponible: {instructor['disponible']}")
            return