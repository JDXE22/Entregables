from helpers import funciones_txt as funciones

def verificar_cliente(cliente):
    clientes = funciones.leer_archivo_txt("clientes")
    for registro in clientes:
        if int(registro['documento']) == cliente:
            return True
    return False

def verificar_disponibilidad_instructor(instructor, fecha, hora):
    citas = funciones.leer_archivo_txt("citas_clientes")
    for cita in citas:
        if cita['instructor'] == instructor and cita['fecha'] == fecha and cita['hora'] == hora:
            return False
    return True

def verificar_existencia_vehiculo(tipo_vehiculo=None):
    vehiculos = funciones.leer_archivo_txt("vehiculos")
    if not vehiculos:
        return False
    if tipo_vehiculo:
        return any(v.get("tipo") == tipo_vehiculo for v in vehiculos)
    return True

def verificar_disponibilidad_vehiculo(vehiculo, fecha, hora):
    vehiculos = funciones.leer_archivo_txt("vehiculos")
    citas = funciones.leer_archivo_txt("citas_clientes")
    
    total_flota = sum(1 for v in vehiculos if v.get("tipo") == vehiculo)
    if total_flota == 0:
        return False

    citas_ocupadas = sum(1 for cita in citas if cita.get('vehiculo') == vehiculo and cita.get('fecha') == fecha and cita.get('hora') == hora)
    
    if citas_ocupadas >= total_flota:
        return False
    return True

def verificar_disponibilidad_bloque(fecha, bloque, tipo_vehiculo=None):
    hora_inicio = bloque["hora"].split(" - ")[0]
    citas = funciones.leer_archivo_txt("citas_clientes")
    for cita in citas:
        if cita['fecha'] == fecha and cita['hora'] == hora_inicio:
            if tipo_vehiculo is None or cita['vehiculo'] == tipo_vehiculo:
                return False
    return True

def verificar_especialidad_instructor(instructor_nombre, tipo_vehiculo):
    instructores = funciones.leer_archivo_txt("instructores")
    nombre_upper = instructor_nombre.strip().upper()
    for inst in instructores:
        if inst['nombre'].upper() == nombre_upper:
            especialidad = inst['especialidad']
            if tipo_vehiculo == "Moto" and especialidad in ["Moto", "Ambos (Carro y Moto)"]:
                return True
            elif tipo_vehiculo == "Carro" and especialidad in ["Carro", "Ambos (Carro y Moto)"]:
                return True
            else: 
                return False
    return False