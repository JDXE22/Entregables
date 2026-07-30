from helpers.funciones import leer_archivo

def verificar_cliente(cliente):
    evaluaciones = leer_archivo("evaluaciones")
    for registro in evaluaciones:
        if registro['cliente'] == cliente:
            return True
    return False
