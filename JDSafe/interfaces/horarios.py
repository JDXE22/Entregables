from datetime import datetime
from helpers import funciones_txt as funciones

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

def mostrar_horarios_disponibles(fecha_f=None):
    if fecha_f is None:
        while True:
            try:
                fecha = input("Ingresar la fecha a consultar (formato DD/MM/YY): \n")
                fecha_f = datetime.strptime(fecha, "%d/%m/%y").strftime("%d/%m/%y")
                break
            except ValueError:
                print("El formato de la fecha ingresada no es valido, por favor ingrese la fecha en el formato DD/MM/YY \n")

    citas_existentes = funciones.leer_archivo_txt("citas_clientes")
    print(f"\n--- Horarios Disponibles (8:00 AM - 5:00 PM) para el {fecha_f} ---")
    for bloque in BLOQUES:
        hora_inicio = bloque["hora"].split(" - ")[0]
        ocupado = False
        estudiante_doc = None
        for c in citas_existentes:
            if c["fecha"] == fecha_f and c["hora"] == hora_inicio:
                ocupado = True
                estudiante_doc = c["cliente"]
                break
        
        estado = f"RESERVADO ({estudiante_doc})" if ocupado else "LIBRE"
        print(f"  {bloque['hora']} --> [{estado}]")
