from datetime import datetime
from helpers import funciones_txt as funciones
from helpers import validaciones
from interfaces.horarios import mostrar_horarios_disponibles, BLOQUES

def agendar_cita():
    while True:
        try:
            cliente = input("Ingresar numero de documento de 10 digitos del cliente, sin comas o espacios. \n")
            sin_espacios = cliente.replace(" ", "")
            if sin_espacios.isdigit():
                tamaño = funciones.calcular_tamaño(cliente)
                if tamaño == 10:
                    cliente = int(cliente)
                    existe = validaciones.verificar_cliente(cliente)
                    if not existe:
                        print("El cliente no está registrado. Por favor, registre al cliente antes de agendar una cita.")
                        return

                    instructor = input("Seleccione el instructor con el que desea tener la clase \n")
                    vehiculo = input("Seleccione el tipo de vehiculo: 1. Moto 2. Carro \n")
                    if vehiculo == "1":
                        vehiculo = "Moto"
                    elif vehiculo == "2": 
                        vehiculo = "Carro"
                    else: 
                        print("Opcion de vehiculo no valida, por favor ingrese una opcion valida")
                        return

                    if not validaciones.verificar_especialidad_instructor(instructor, vehiculo):
                        print(f"El instructor {instructor} no tiene especialidad para enseñar a manejar {vehiculo}. Seleccione otro instructor.")
                        continue
                    
                    while True:
                        try:
                            fecha_insertada = input("Ingrese en formato DD/MM/YY la fecha de la cita \n")
                            fecha_f = datetime.strptime(fecha_insertada, "%d/%m/%y").strftime("%d/%m/%y")
                            break
                        except ValueError:
                            print("El formato de la fecha ingresada no es valido. Por favor use el formato DD/MM/YY (ej. 24/07/26).\n")
                    
                    mostrar_horarios_disponibles(fecha_f)
                    
                    while True:
                        try:
                            opcion_bloque = int(input("\nSeleccione el numero del bloque de horario a agendar (1-9): "))
                            if 1 <= opcion_bloque <= len(BLOQUES):
                                bloque_sel = BLOQUES[opcion_bloque - 1]
                                hora_f = bloque_sel["hora"].split(" - ")[0]
                                break
                            else:
                                print(f"Opcion invalida. Debe ser un numero entre 1 y {len(BLOQUES)}.\n")
                        except ValueError:
                            print("Entrada invalida. Por favor, ingrese un numero entero.\n")

                    if not validaciones.verificar_disponibilidad_instructor(instructor, fecha_f, hora_f):
                        print(f"El instructor {instructor} no está disponible en la fecha y hora seleccionadas.")
                        continue

                    if not validaciones.verificar_disponibilidad_vehiculo(vehiculo, fecha_f, hora_f):
                        print(f"El vehículo {vehiculo} no está disponible en la fecha y hora seleccionadas.")
                        continue
                    if not validaciones.verificar_disponibilidad_cita(fecha_f, hora_f):
                        print(f"Ya existe una cita programada en la fecha {fecha_f} y hora {hora_f}. Por favor, seleccione otra fecha y hora.")
                        continue

                else:
                    print("El documento debe tener exactamente 10 dígitos. Intente de nuevo.\n")
                    continue
            else:
                print("El documento ingresado no es válido. Debe contener solo números.\n")
                continue

        except ValueError:
            print("El dato ingresado no es valido, por favor ingrese un dato valido \n")
        except TypeError as e:
            print(f"Se ha ingresado un dato no valido {e}\n")
        except Exception as e:
            print(f"Se ha presentado un error inesperado {e}\n")
        else: 
            cita = {
                "cliente": cliente,
                "instructor": instructor,
                "vehiculo": vehiculo,
                "fecha": fecha_f,
                "hora": hora_f
            }      
            funciones.crear_archivo_txt("citas_clientes", cita)
            print("Cita agendada correctamente")
            print(f"Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Fecha: {cita['fecha']}, Hora: {cita['hora']} \n")
            return

def consultar_citas_por_cliente():
    citas = funciones.leer_archivo_txt("citas_clientes")

    while True:
        try:
            cliente = input("Ingresar numero de documento de 10 digitos del cliente, sin comas o espacios. \n")
            if cliente.isdigit() and len(cliente) == 10:
                cliente = int(cliente)
                encontradas = [cita for cita in citas if cita['cliente'] == cliente]
                if encontradas:
                    print(f"Se han encontrado los siguientes resultados del cliente: {cliente}")
                    for cita in encontradas:
                        print(f"Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Fecha: {cita['fecha']}, Hora: {cita['hora']} \n")
                else:
                    print("No se encontraron citas para el cliente ingresado.\n")
                return
            else:
                print("El documento ingresado no es válido. Debe contener exactamente 10 dígitos.\n")
        except ValueError:
            print("El documento ingresado no es valido, por favor ingrese un numero de documento valido \n")
        except Exception as e:
            print(f"Se ha presentado un error inesperado {e}\n")

def consultar_citas_por_fecha():
    citas = funciones.leer_archivo_txt("citas_clientes")

    while True:
        try:
            fecha = input("Ingresar la fecha de la cita programada (formato DD/MM/YY): \n")
            fecha_f = datetime.strptime(fecha, "%d/%m/%y").strftime("%d/%m/%y")
            encontradas = [cita for cita in citas if cita['fecha'] == fecha_f]
            if encontradas:
                print(f"Se han encontrado los siguientes resultados de la fecha: {fecha_f} \n")
                for cita in encontradas:
                    print(f"Cliente: {cita['cliente']}, Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Hora: {cita['hora']} \n")
            else:
                print("No se encontraron citas para la fecha ingresada.\n")
            return
        except ValueError:
            print("El formato de la fecha ingresada no es valido, por favor ingrese la fecha en el formato DD/MM/YY \n")
        except Exception as e:
            print(f"Se ha presentado un error inesperado {e}\n")