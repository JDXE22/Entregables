from datetime import datetime
from helpers import funciones_txt as funciones

def registrar_asistencia_y_observacion():
    while True:
        try:
            codigo = int(input("Ingrese el codigo de la cita (numero de 3 digitos): \n"))
            break
        except ValueError:
            print("El dato ingresado no es valido. Por favor ingrese un numero de cita de 3 digitos.\n")

    citas = funciones.leer_archivo_txt("citas_clientes")
    cita_existente = next((c for c in citas if c.get("codigo") == codigo), None)
    if not cita_existente:
        print(f"No se encontro ninguna cita programada con el codigo {codigo}. Por favor verifique el codigo.")
        return

    existe = funciones.leer_archivo_txt("asistencias")
    for a in existe:
        if a["codigo"] == codigo:
            print(f"Ya existe una asistencia y observacion registrada para la cita {codigo}")
            return
    
    observacion = input("Ingrese la observacion de la asistencia: \n")
    fecha_str = cita_existente["fecha"]

    asistencia = {"codigo": codigo, "fecha": fecha_str, "observacion": observacion}
    funciones.crear_archivo_txt("asistencias", contenido=asistencia)
    print("Asistencia y observacion registrada correctamente")
    print(f"Codigo de cita: {codigo}")
    print(f"Fecha: {fecha_str}")
    print(f"Observacion: {observacion}")

def consultar_asistencia_y_observacion():
    while True:
        try:
            cita = int(input("Ingrese el codigo de la cita recuerde que es un numero de 3 digitos: \n"))
            break
        except ValueError:
            print("El dato ingresado no es valido, por favor ingrese un numero de cita valido\n")
            continue

    try:
        existe = funciones.leer_archivo_txt("asistencias")
        for asistencia in existe:
            if asistencia["codigo"] == cita:
                print(f"Codigo de cita: {asistencia['codigo']}")
                print(f"Fecha: {asistencia['fecha']}")
                print(f"Observacion: {asistencia['observacion']}")
                return
        print("No se encontro una asistencia y observacion registrada para esta cita")
    except Exception as e:
        print(f"Se ha presentado un error inesperado {e}\n")

def menu_asistencias():
    while True:
        try:
            print("1. Registrar asistencia y observacion")
            print("2. Consultar asistencia y observacion")
            print("Ingrese 0 para salir")
            opcion = int(input("Ingrese la opcion: \n"))    
        except ValueError:
            print("Se ha ingresado una opcion no valida\n")
        except Exception as e: 
            print(f"Se ha presentado un error inesperado {e}\n")
        else:
            if opcion == 1: 
                registrar_asistencia_y_observacion()
            elif opcion == 2:
                consultar_asistencia_y_observacion()
            elif opcion == 0:
                print("Saliendo del menu de asistencias y observaciones... \n")
                break
