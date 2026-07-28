from datetime import datetime
import random
from helpers import funciones_txt as funciones
from helpers import validaciones
from interfaces.horarios import mostrar_horarios_disponibles, BLOQUES

def agendar_cita():
    print("\n" + "="*50)
    print("      SISTEMA DE AGENDAMIENTO DE CITAS")
    print("="*50)
    
    print("\n--- Clientes Registrados ---")
    lista_clientes = funciones.leer_archivo_txt("clientes")
    if not lista_clientes:
        print(" No hay clientes registrados en el sistema.")
    else:
        for c in lista_clientes:
            print(f"  • Nombre: {c['nombre']} | Documento: {c['documento']} | Curso: {c['curso']}")
    print("-" * 50 + "\n")

    while True:
        cliente = input("Ingresar numero de documento de 6 a 10 digitos del cliente, sin comas o espacios. \n")
        sin_espacios = cliente.replace(" ", "")
        if not sin_espacios.isdigit():
            print("El documento ingresado no es válido. Debe contener solo números.\n")
            continue
        
        tamano = funciones.calcular_tamaño(cliente)
        if not (6 <= tamano <= 10):
            print("\n El documento debe tener entre 6 y 10 dígitos. Intente de nuevo.\n")
            continue
        
        cliente = int(sin_espacios)
        existe = validaciones.verificar_cliente(cliente)
        if not existe:
            print("El cliente no está registrado. Por favor, registre al cliente antes de agendar una cita.")
            return
        break

    if not validaciones.verificar_existencia_vehiculo():
        print("No hay vehículos registrados en el sistema. Por favor, registre al menos un vehículo antes de agendar una cita.")
        return

    while True:
        vehiculo = input("Seleccione el tipo de vehiculo: 1. Moto 2. Carro \n")
        if vehiculo == "1":
            if not validaciones.verificar_existencia_vehiculo("Moto"):
                print("No hay vehículos de tipo Moto registrados en el sistema. Por favor, registre una Moto primero.\n")
                continue
            vehiculo = "Moto"
            break
        elif vehiculo == "2": 
            if not validaciones.verificar_existencia_vehiculo("Carro"):
                print("No hay vehículos de tipo Carro registrados en el sistema. Por favor, registre un Carro primero.\n")
                continue
            vehiculo = "Carro"
            break
        else: 
            print("Opcion de vehiculo no valida, por favor ingrese una opcion valida")
            
    print(f"\nBuscando instructores disponibles para la especialidad: {vehiculo}...\n")
    instructores_registrados = funciones.leer_archivo_txt("instructores")
    instructores_filtrados = []
    for inst in instructores_registrados:
        especialidad = inst["especialidad"]
        if vehiculo == "Moto" and especialidad in ["Moto", "Ambos (Carro y Moto)"]:
            instructores_filtrados.append(inst)
        elif vehiculo == "Carro" and especialidad in ["Carro", "Ambos (Carro y Moto)"]:
            instructores_filtrados.append(inst)

    if not instructores_filtrados:
        print(f"No hay instructores registrados o disponibles para enseñar {vehiculo}. Por favor registre un instructor primero.")
        return

    print(f"\n--- Instructores Disponibles para {vehiculo} ---")
    for i, inst in enumerate(instructores_filtrados, start=1):
        print(f"  {i}. {inst['nombre']} (Especialidad: {inst['especialidad']})")

    while True:
        try:
            opcion_inst = int(input(f"\nSeleccione el numero del instructor (1-{len(instructores_filtrados)}): "))
            if 1 <= opcion_inst <= len(instructores_filtrados):
                instructor = instructores_filtrados[opcion_inst - 1]["nombre"]
                break
            else:
                print(f"Opcion invalida. Debe ser un numero entre 1 y {len(instructores_filtrados)}.\n")
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero entero.\n")

    while True:
        while True:
            try:
                fecha_insertada = input("Ingrese la fecha de la cita (formato DD/MM/YY): \n")
                fecha_usuario_obj = datetime.strptime(fecha_insertada, "%d/%m/%y")
                fecha_actual_obj = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if fecha_usuario_obj < fecha_actual_obj:
                    print("La fecha ingresada es en el pasado. Por favor, ingrese una fecha válida (hoy o futura).\n")
                    continue
                fecha_f = fecha_usuario_obj.strftime("%d/%m/%y")
                break
            except ValueError:
                print("\nEl formato de la fecha ingresada no es válido. Debe ser DD/MM/YY (ej. 30/07/26).\n")                               

        mostrar_horarios_disponibles(fecha_f)
        
        while True:
            try:
                opcion_bloque = int(input(f"\nSeleccione el numero del bloque de horario a agendar (1-{len(BLOQUES)}): "))
                if 1 <= opcion_bloque <= len(BLOQUES):
                    bloque_sel = BLOQUES[opcion_bloque - 1]
                    hora_f = bloque_sel["hora"].split(" - ")[0]
                    break
                else:
                    print(f"Opcion invalida. Debe ser un numero entre 1 y {len(BLOQUES)}.\n")
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero entero.\n")

        if not validaciones.verificar_disponibilidad_instructor(instructor, fecha_f, hora_f):
            print(f"El instructor {instructor} no está disponible en la fecha y hora seleccionadas. Por favor seleccione otra fecha u hora.\n")
            continue

        if not validaciones.verificar_disponibilidad_vehiculo(vehiculo, fecha_f, hora_f):
            print(f"El vehículo {vehiculo} no está disponible en la fecha y hora seleccionadas. Por favor seleccione otra fecha u hora.\n")
            continue
            
        break

    citas_existentes = funciones.leer_archivo_txt("citas_clientes")
    while True:
        codigo = random.randint(100, 999)
        if not any(c.get("codigo") == codigo for c in citas_existentes):
            break

    cita = {
        "codigo": codigo,
        "cliente": cliente,
        "instructor": instructor,
        "vehiculo": vehiculo,
        "fecha": fecha_f,
        "hora": hora_f
    }      
    funciones.crear_archivo_txt("citas_clientes", cita)
    print("Cita agendada correctamente")
    print(f"Codigo de cita: {codigo}")
    print(f"Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Fecha: {cita['fecha']}, Hora: {cita['hora']} \n")
    return

def consultar_citas_por_cliente():
    citas = funciones.leer_archivo_txt("citas_clientes")

    while True:
        try:
            cliente = input("Ingresar numero de documento de 6 a 10 digitos del cliente, sin comas o espacios. \n")
            tamano = funciones.calcular_tamaño(cliente)
            if cliente.isdigit() and 6 <= tamano <= 10:
                cliente = int(cliente)
                encontradas = [cita for cita in citas if cita['cliente'] == cliente]
                if encontradas:
                    print(f"Se han encontrado los siguientes resultados del cliente: {cliente}")
                    for cita in encontradas:
                        print(f"Codigo: {cita.get('codigo', 'N/A')}, Instructor: {cita['instructor']}, Vehiculo: {cita['vehiculo']}, Fecha: {cita['fecha']}, Hora: {cita['hora']} \n")
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
            print("\n" + "="*50)
            print(f"Citas Agendadas para el {fecha_f}")
            print("="*50)
            if encontradas:
                print(f"Se han encontrado los siguientes resultados de la fecha: {fecha_f} \n")
                for i, cita in enumerate(encontradas, 1):
                    print(f"  Cita #{i}:")
                    print(f"    • Código: {cita.get('codigo', 'N/A')}")
                    print(f"    • Cliente (Doc): {cita['cliente']}")
                    print(f"    • Instructor: {cita['instructor']}")
                    print(f"    • Vehículo: {cita['vehiculo']}")
                    print(f"    • Hora: {cita['hora']} (Inicio)")
                    print("    " + "-"*30)
            else:
                print("No se encontraron citas para la fecha ingresada.")
                print("="*50 + "\n")
            return
        except ValueError:
            print("El formato de la fecha ingresada no es valido, por favor ingrese la fecha en el formato DD/MM/YY \n")
        except Exception as e:
            print(f"Se ha presentado un error inesperado {e}\n")