from helpers import funciones_txt as funciones
from helpers import validaciones 

def mostrar_horarios_disponibles():
    agenda_del_dia = funciones.leer_archivo_txt("horarios_base")
    print("\n--- Horarios Disponibles (8:00 AM - 5:00 PM) ---")
    for i, bloque in enumerate(agenda_del_dia, start=1):
        estado = "LIBRE" if bloque["disponible"] else f"RESERVADO ({bloque['estudiante']})"
        print(f"{i}. {bloque['hora']} --> [{estado}]")

def agendar_clase():
    agenda_del_dia = funciones.leer_archivo_txt("horarios_base")
    mostrar_horarios_disponibles()
    try:
        opcion = int(input("\nSeleccione el número del bloque a agendar: ")) - 1
        
        if 0 <= opcion < len(agenda_del_dia):
            bloque = agenda_del_dia[opcion]
            
            if not bloque["disponible"]:
                print("Ese horario ya está ocupado.")
                return None
            
            estudiante = input("Ingrese el número de documento del estudiante (10 dígitos): ")
            if estudiante.isdigit() and len(estudiante) == 10:
                estudiante = int(estudiante)
            else:
                print("El documento ingresado no es válido. Debe contener exactamente 10 dígitos.")
                return None
            existe = validaciones.verificar_cliente(estudiante)
            if not existe:
                print("El estudiante no está registrado. Por favor, registre al estudiante antes de agendar una clase.")
                return None
          
            bloque["disponible"] = False
            bloque["estudiante"] = estudiante
            funciones.actualizar_archivo_txt("horarios_base", agenda_del_dia)
            print(f"¡Clase agendada exitosamente a las {bloque['hora']} para {estudiante}!")
            return opcion
        else:
            print("Opción fuera de rango.")
    except ValueError:
        print("Entrada inválida.")
    return None
