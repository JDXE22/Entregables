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
    while True:
        try:
            if fecha is not None:
                    print(f"Mostrando horarios disponibles para la fecha: {fecha}")
                    horarios_filtrados = [bloque for bloque in BLOQUES if validaciones.verificar_disponibilidad_bloque(fecha, bloque)]
            else:
                    print("Mostrando todos los horarios disponibles para el dia de hoy:")
                    horarios_filtrados = BLOQUES

            for i, bloque in enumerate(horarios_filtrados, start=1):
                    print(f"{i}. {bloque['hora']}")

            if fecha is None:
                print("\nNota: Los horarios mostrados son para el día de hoy. Para ver horarios de otra fecha, ingrese la fecha deseada.")
                fecha_input = input("Ingrese la fecha en formato DD/MM/YY para ver horarios disponibles (o presione Enter para continuar): ")
                if fecha_input:
                    fecha_f = datetime.strptime(fecha_input, "%d/%m/%y").strftime("%d/%m/%y")
                    mostrar_horarios_disponibles(fecha_f)

        except ValueError:
            print("El formato de la fecha ingresada no es valido. Por favor use el formato DD/MM/YY (ej. 24/07/26).")
                        