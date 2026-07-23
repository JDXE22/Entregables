from helpers import funciones_txt as funciones

def mostrar_horarios_disponibles():
    agenda_del_dia = funciones.leer_archivo_txt("horarios_base")
    print("\n--- Horarios Disponibles (8:00 AM - 5:00 PM) ---")
    for i, bloque in enumerate(agenda_del_dia, start=1):
        estado = "LIBRE" if bloque["disponible"] else f"RESERVADO ({bloque['estudiante']})"
        print(f"{i}. {bloque['hora']} --> [{estado}]")

def agendar_clase():
    agenda_del_dia = funciones.leer_archivo_txt("horarios")
    mostrar_horarios_disponibles()
    try:
        opcion = int(input("\nSeleccione el número del bloque a agendar: ")) - 1
        
        if 0 <= opcion < len(agenda_del_dia):
            bloque = agenda_del_dia[opcion]
            
            if not bloque["disponible"]:
                print("Ese horario ya está ocupado.")
                return None
            
            estudiante = input("Nombre del estudiante: ").strip()
            bloque["disponible"] = False
            bloque["estudiante"] = estudiante
            print(f"¡Clase agendada exitosamente a las {bloque['hora']} para {estudiante}!")
            return opcion
        else:
            print("Opción fuera de rango.")
    except ValueError:
        print("Entrada inválida.")
    return None
