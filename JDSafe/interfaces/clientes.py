from io import open
print("Bienvenido al sistema de creacion de clientes")

#min 6 maximo 50 para el nombre
while True:
    try:
        nombre = input("Ingrese su primer nombre y primer apellido: \n")
        tamaño=nombre.replace(" ","").__len__()
        if (tamaño < 6 and tamaño > 50):
            print("Nombre invalido, ingresar de nuevo")

    except ValueError as e:
            print("Se ingreso un tipo de dato diferente a una cadena de texto, por favor ingrese solo texto")
            print(f"Se ha presentado el siguiente error: {e}")
    else: 
        print(f"El tamaño de el nombre es {tamaño}")
        print("Saliendo")

#documento = int(input("Ingrese el numero de documento: \n"))

# #while len(documento) == 10:
# #   try:
#         print("Ingrese un numero de documento valido de 10 digitos")
        
# #    except ValueError as e:
#         print(f"Se ha presentado el siguiente error: {e}")

# #    else: 
#         break





