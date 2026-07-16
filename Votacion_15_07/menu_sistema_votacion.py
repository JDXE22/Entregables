import sistema_votacion

while True:
    print("Bienvenido al menu de sistema de votaciones")
    print("Seleccione una operacion del siguiente menu: \n")
    print("1. Registrar el voto")
    print("2. Mostrar los resultados")
    print("3. Determinar ganador")
    print("Ingrese 'FIN' para terminar las votaciones y ver los resultados finales")

    opcion = input("Ingrese las opciones del menu 1/2/ o 3 \n")

    if opcion == "1":
        sistema_votacion.registrar_voto()
    elif opcion == "2":
        sistema_votacion.mostrar_resultados()
    elif opcion == "3":
        ganador,votos, empatados = sistema_votacion.determinar_ganador()
        if(ganador is None):
            print("No hay candidatos registrados")
        elif len(empatados) > 1: 
            print(f"Empate entre: {','.join(empatados)} con {votos} votos, toca hacer segunda vuelta")
        else:
            print(f"El ganador es {ganador} con {votos} votos")
    elif opcion.upper() == "FIN":
        break
    else:
        print("Opcion no valida")
    
    
    
