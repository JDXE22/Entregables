from helpers import funciones
from datetime import datetime


def registrar_evaluacion():
    while True:
        try:
            print("Bienvenido al sistema de registro de evaluaciones de prácticas de manejo.\n")
            print("Por favor, ingrese los datos del cliente y la evaluación de la práctica.\n") 

            nombre_cliente = input("Ingrese el primer nombre y apellido del cliente \n").strip().replace(" ", "")
            if nombre_cliente.isalpha():
                tamano = funciones.calcular_tamaño(nombre_cliente)
                if 6 <= tamano <= 50:
                    nombre_cliente = nombre_cliente.upper() 
                    print(f"Nombre válido. Bienvenido/a, {nombre_cliente}\n")
                    break
                else:
                    print(f"El nombre solo contiene letras, pero su longitud ({tamano}) debe estar entre 6 y 50 caracteres.")
                    print("Intente de nuevo.\n")
            else:
                print("El nombre ingresado no es válido. No debe contener números ni símbolos.")
                print("Intente de nuevo.\n")

        except ValueError:
            print("El nombre ingresado no es válido. Debe contener solo letras.")
            print("Intente de nuevo.\n")
            continue
            
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")
            print("Intente de nuevo.\n")
            continue

    
    while True:
        try:
            nombre_instructor = input("Ingrese el primer nombre y apellido del instructor \n").strip().replace(" ", "")
            if nombre_instructor.isalpha():
                tamano = funciones.calcular_tamaño(nombre_instructor)
                if 6 <= tamano <= 50:
                    nombre_instructor = nombre_instructor.upper() 
                    print(f"Nombre válido. Bienvenido/a instructor, {nombre_instructor}\n")
                    break
                else:
                    print(f"El nombre solo contiene letras, pero su longitud ({tamano}) debe estar entre 6 y 50 caracteres.")
                    print("Intente de nuevo.\n")
            else:
                print("El nombre ingresado no es válido. No debe contener números ni símbolos.")
                print("Intente de nuevo.\n")

        except ValueError:
            print("El nombre ingresado no es válido. Debe contener solo letras.")
            print("Intente de nuevo.\n")
            continue
            
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")
            print("Intente de nuevo.\n")
            continue

        else: 
            print(f"El nombre solo contiene letras, pero su longitud ({tamano}) debe estar entre 6 y 50 caracteres.")
            print("Intente de nuevo.\n")

    while True:
            try:
                fecha_insertada = input("Ingrese la fecha de la evaluacion (formato YYYY-MM-DD): \n")
                fecha_usuario_obj = datetime.strptime(fecha_insertada, "%Y/%m/%d")
                fecha_actual_obj = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if fecha_usuario_obj < fecha_actual_obj:
                    print("La fecha ingresada es en el pasado. Por favor, ingrese una fecha válida (hoy o futura).\n")
                    continue
                fecha_f = fecha_usuario_obj.strftime("%Y/%m/%d")
                break
            except ValueError:
                print("\nEl formato de la fecha ingresada no es válido. Debe ser YYYY-MM-DD (ej. 2025/02/10).\n")

    while True:
        print("Ingrese la calificacion del cliente, tenga en cuenta que la calificacion debe ser un numero entero \n")
        print("y debe estar entre 0 y 100, donde 0 es la calificacion mas baja y 100 es la calificacion mas alta \n")
        try:
            calificacion_cliente = int(input("Ingrese la calificacion del cliente"))
            if 0 <= calificacion_cliente <= 100:
                print(f"Calificacion valida. La calificacion del cliente es: {calificacion_cliente}\n")
                break
            else:
                print("La calificacion no es valida, por favor ingrese el numero nuevamente")
                continue

        except ValueError:
            print("\nEl formato de la fecha ingresada no es válido. Debe ser YYYY-MM-DD (ej. 2025/02/10).\n")
    
    nueva_entrada = {
        "estudiante": nombre_cliente,
        "instructor": nombre_instructor,
        "fecha_evaluacion": fecha_f,
        "calificacion": calificacion_cliente
    }

    funciones.crear_archivo("evaluaciones", nueva_entrada)
    print("La evaluacion ha sido creada exitosamente \n")

def consulta_estudiante():
    evaluaciones = funciones.leer_archivo("evaluaciones")
    print("Consultando evaluaciones de las practicas por cliente")
    print("Ingrese el nombre del cliente para consultar sus evaluaciones")
    while True:
        try:
            nombre_cliente = input("Ingrese el primer nombre y apellido del cliente \n").strip().replace(" ", "")
            print(nombre_cliente)
            if nombre_cliente.isalpha():
                tamano = funciones.calcular_tamaño(nombre_cliente)
                if 6 <= tamano <= 50:
                    nombre_cliente = nombre_cliente.upper() 
                    print(f"Nombre válido. Bienvenido/a, {nombre_cliente}\n")
                    encontradas = [cliente for cliente in evaluaciones if cliente['estudiante'] == nombre_cliente]
                    if encontradas:
                        print(f"Se han encontrado los siguientes resultados del cliente: {nombre_cliente}")
                        for cliente in encontradas:
                            print(f"Nombre del cliente: {cliente['estudiante']}, Nombre del instructor: {cliente['instructor']}, Fecha de la evaluacion: {cliente['fecha_evaluacion']}, Calificacion: {cliente['calificacion']}")
                    else:
                        print("No se encontraron citas para el cliente ingresado.\n")
                        return
                else:
                    print(f"El nombre solo contiene letras, pero su longitud ({tamano}) debe estar entre 6 y 50 caracteres.")
                    print("Intente de nuevo.\n")
            else:
                print("El nombre ingresado no es válido. No debe contener números ni símbolos.")
                print("Intente de nuevo.\n")

        except ValueError:
            print("El nombre ingresado no es válido. Debe contener solo letras.")
            print("Intente de nuevo.\n")
            continue
            
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")
            print("Intente de nuevo.\n")
            continue



