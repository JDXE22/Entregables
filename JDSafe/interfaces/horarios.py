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

def mostrar_horarios_disponibles(fecha=None):
    if fecha:
        print(f"Mostrando horarios disponibles para la fecha: {fecha}")
        horarios_filtrados = [bloque for bloque in BLOQUES if validaciones.verificar_disponibilidad_bloque(fecha, bloque)]
    else:
        print("Mostrando todos los horarios disponibles para el dia de hoy:")
        horarios_filtrados = BLOQUES

    for i, bloque in enumerate(horarios_filtrados, start=1):
        print(f"{i}. {bloque['hora']}")

    return horarios_filtrados