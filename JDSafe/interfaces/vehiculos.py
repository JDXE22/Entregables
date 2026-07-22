from ..helpers import funciones_txt as funciones

print("Bienvenido al sistema de agregado de vehiculos")
print("Dentro de este formulario debe de ingresar los siguientes datos")
print("1. Seleccionar tipo de vehiculo (Moto o Carro)")
print("2. Ingresar placa de el vehiculo")

while True:
        try:
                print("Seleccione tipo de vehiculo \n")
                print("1. Moto")
                print("2. Carro")
                opcion = int(input())
                if opcion == 1:
                        print("El vehiculo es Moto")
                        sel = "Moto"
                        
                elif opcion == 2:
                        print("El vehiculo es Carro")
                        sel = "Carro"

                else:
                       print("No fueron ingresadas ninguna de las opciones validas")

                print(f"El vehiculo seleccionado para aprender fue {sel}")
                print("Ingrese 0 para confirmar y salir de el programa")
                sal = int(input())   
                if sal == 0:
                       print("Saliendo")
                       break
                else:
                       print("Confirmación cancelada, Iniciando nuevamente menú de seleccion de vehiculos")
        except ValueError as e:
               print(f"El dato ingresado no es valido, por lo que genera un error {e}")


while True:
        placa = (input(f"Ingrese la placa para {sel} sin espacios ni guiones: \n")).replace(" ","").upper
        validacion = len(placa)
        if validacion != 6:
             print(f"la placa debe de tener un tamaño de 6, no es valida la placa {placa} (ej. ABC123 o ABC12D).\n ")
             print("ingrese nuevamente una placa")
             continue
        
        letras_placa = placa[0:3]
        if not placa.isalpha: 
            print("Los primeros 3 caracteres deben ser letras")
            print("ingrese nuevamente una placa")
            continue
        if sel == "Carro":
            numeros = placa[3:6]
            if numeros.isdigit():
                print(f"Placa de Carro válida: {placa}")
                break
            else:
                print("Error: Los últimos 3 caracteres para un carro deben ser números (ej. ABC123).\n")
            
        elif sel == "Moto":
            numeros = placa[3:5]
            letra_final = placa[5]
            if numeros.isdigit() and letra_final.isalpha():
                print(f"Placa de Moto válida: {placa}")
                break
        else:
            print("Error: La placa de moto debe tener 2 números y terminar en una letra (ej. ABC12D).\n")    


vehiculo_Nuevo = (
       "Registro de vehiculo nuevo \n"
       f"Tipo de Vehiculo: {sel} \n"
       f"Placa: {placa} \n"
       "\n\n\n"
)

funciones.crear_archivo_txt("data/vehiculos", vehiculo_Nuevo)