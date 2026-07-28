from datetime import datetime
from helpers import funciones_txt as funciones
from helpers import validaciones

BLOQUES = [
    {"hora": "08:00 - 09:00", "disponible": True, "estudiante": None},
    {"hora": "09:00 - 10:00", "disponible": True, "estudiante": None},
    {"hora": "10:00 - 11:00", "disponible": True, "estudiante": None},
    {"hora": "11:00 - 12:00", "disponible": True, "estudiante": None},
    {"hora": "12:00 - 13:00", "disponible": True, "estudiante": None},
    {"hora": "13:00 - 14:00", "disponible": True, "estudiante": None},
    {"hora": "14:00 - 15:00", "disponible": True, "estudiante": None},
    {"hora": "15:00 - 16:00", "disponible": True, "estudiante": None},
    {"hora": "16:00 - 17:00", "disponible": True, "estudiante": None},
]

def mostrar_horarios_disponibles(fecha=None, interactivo=False):
    if fecha is None:
        fecha = datetime.now().strftime("%d/%m/%y")
        print(f"\n--- Horarios Disponibles (8:00 AM - 5:00 PM) para el {fecha} ---")
    else:
        print(f"\n--- Horarios Disponibles (8:00 AM - 5:00 PM) para el {fecha} ---")

    for i, bloque in enumerate(BLOQUES, start=1):
        disponible = validaciones.verificar_disponibilidad_bloque(fecha, bloque)
        estado = "[LIBRE]" if disponible else "[OCUPADO]"
        print(f"  {i}. {bloque['hora']} --> {estado}")

    if interactivo:
        while True:
            try:
                fecha_input = input("\n¿Desea consultar otra fecha? Ingrese una fecha (DD/MM/YY) o presione Enter para salir: ").strip()
                if not fecha_input:
                    break
                fecha_f = datetime.strptime(fecha_input, "%d/%m/%y").strftime("%d/%m/%y")
                mostrar_horarios_disponibles(fecha_f, interactivo=True)
                break
            except ValueError:
                print("La fecha insertada no es valida. Por favor use el formato DD/MM/YY (ej. 27/07/26).\n")

    return BLOQUES