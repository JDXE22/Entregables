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

def verificar_disponibilidad_vehiculo(vehiculo, fecha, hora):
    citas = funciones.leer_archivo_txt("citas_clientes")
    for cita in citas:
        if cita['vehiculo'] == vehiculo and cita['fecha'] == fecha and cita['hora'] == hora:
            return False
    return True

def verificar_disponibilidad_cita(fecha,hora):
    citas = funciones.leer_archivo_txt("citas_clientes")
    for cita in citas:
        if cita['fecha'] == fecha and cita['hora'] == hora:
            return False
    return True

def verificar_especialidad_instructor(especialidad):
    instructores = funciones.leer_archivo_txt("instructores")
    for instructor in instructores:
        if instructor['especialidad'] ==  especialidad:
            return False
    return True 
    