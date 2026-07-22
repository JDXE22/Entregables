from ..helpers import funciones_txt as funciones

print("Bienvenido al sistema de creacion de clientes")
print("Dentro de este formulario debe de ingresar los siguientes datos")
print("1. Primer nombre y primer apellido")
print("2. Numero de documento")
print("3. Seleccionar curso de aprendizaje (Moto, carro o ambos)")


while True:
        nombre = (input("Ingrese su primer nombre y primer apellido: \n"))
        sin_espacios=nombre.replace(" ","")
        validacion = sin_espacios.isalpha()
        if validacion == True:
             resultado = funciones.calcular_tamaño(nombre)
             print(resultado)
             print(f"El nombre es valido y tiene un tamaño de {resultado}")
             if (6 <= resultado <= 50):
                    nombre.upper()
                    print(f"Bienvenido {nombre}")
                    break
             else: 
                print(f"El nombre tiene solo letras, pero su tamaño ({resultado}) no está entre 6 y 50 caracteres.")
                print("Intente de nuevo.\n")
        else:
            print("El nombre ingresado no fue valido, no debe contener numeros ni simbolos.")
            print("Debe ser ingresado nuevamente.\n")    



while True:
        documento = (input("Ingresar numero de documento de 10 Digitos, sin comas o espacios. \n"))
        sin_espacios=documento.replace(" ","")
        validacion = sin_espacios.isdigit()
        if validacion == True:
                resultadoD = funciones.calcular_tamaño(documento)
                print(resultadoD)
                print(f"El documento tiene un tamaño de {resultadoD} digitos")

                if (resultadoD == 10):
                        print(f"Documento valido: {documento}")
                        print("Saliendo")
                        break

                else:
                        print(f"El Documento tiene solo numeros, pero su tamaño ({resultadoD}) no es de 10 numeros")
                        print("Intente de nuevo con un documento valido.\n")
        else:
                print("El Documento ingresado no fue valido, no debe contener letras ni simbolos.")
                print("Debe ser ingresado nuevamente.\n") 
       

while True:
        try:
                print("Seleccione curso \n")
                print("1. Moto")
                print("2. Carro")
                print("3. Ambos")
                opcion = int(input())
                if opcion == 1:
                        print("Su seleccon fue Moto")
                        sel = "Moto"
                        
                elif opcion == 2:
                        print("Su seleccon fue Carro")
                        sel = "Carro"
                        
                elif opcion == 3:
                        print("Su seleccon fue Ambos (Carro y Moto)")
                        sel = "Ambos (Carro y Moto)"
                else:
                       print("No fueron ingresadas ninguna de las opciones validas")

                print(f"El curso seleccionado fue {sel}")
                print("Ingrese 0 para confirmar y salir de el programa")
                sal = int(input())   
                if sal == 0:
                       print("Saliendo")
                       break
                else:
                       print("Confirmación cancelada, Iniciando nuevamente menú selección de curso")
        except ValueError as e:
               print(f"El dato ingresado no es valido, por lo que genera un error {e}")

Cliente_Nuevo = (
       "Registro de Cliente Nuevo \n"
       f"Nombre: {nombre} \n"
       f"Documento: {documento} \n"
       f"Curso: {sel} \n"
       "\n\n\n"
)

funciones.crear_archivo_txt("clientes", Cliente_Nuevo)