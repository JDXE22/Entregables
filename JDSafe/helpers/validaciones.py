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

def verificar_especialidad_instructor(instructor, tipo_vehiculo):
    instructores = funciones.leer_archivo_txt("instructores")
    for instructor in instructores:
        if instructor['nombre'] == instructor:
            especialidad = instructor['especialidad']
            if tipo_vehiculo == "Moto" and especialidad in ["Moto", "Ambos (Carro y Moto)"]:
                return True
            elif tipo_vehiculo == "Carro" and especialidad in ["Carro", "Ambos (Carro y Moto)"]:
                return True
            else: 
                return False
    return False