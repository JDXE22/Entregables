
candidatos = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Candidato C": 0
}

conteo = 0

def registrar_voto():
    global conteo
    candidato = input("Ingrese el nombre del candidato \n")
    candidato = candidato.strip().upper()
    if candidato == "A":
        conteo += 1
        candidatos["Candidato A"] = candidatos["Candidato A"] + 1
    elif candidato == "B":
        conteo += 1
        candidatos["Candidato B"] = candidatos["Candidato B"] + 1
    elif candidato == "C":
        conteo += 1
        candidatos["Candidato C"] = candidatos["Candidato C"] + 1
    else:
        print("Se ha ingresado un dato no valido, ingrese el valor nuevamente")

def mostrar_resultados():
    for clave, valor in candidatos.items():
        print(f"El candidato {clave} tiene {valor} de votos")

def determinar_ganador():
    if not any(candidatos.values()):
        return None, 0, []
    max_votos = max(candidatos.values())
    ganadores = [clave for clave, votos in candidatos.items() if votos == max_votos]
    return ganadores[0], max_votos, ganadores
    

