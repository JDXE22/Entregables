from io import open

productos = []

def guardarProductosArchivo(productos):
    with open("archivo.txt", "a") as archivo:
        for producto in productos:
            archivo.write(f"{producto[0]},{producto[1]},{producto[2]}\n")

def leerProductosArchivo():
    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            codigo, nombre, valor = linea.strip().split(",")
            productos.append([int(codigo), nombre, float(valor)])


def agregarProducto():
    codigo = int(input("Digite el codigo del producto que se añadira\n"))
    nombre = input("Digite el nombre del producto\n")
    valor = float(input("Digite el valor del producto\n"))
    while len(nombre) == 0:
        print("El nombre del producto no puede estar vacio")
        nombre = input("Digite el nombre del producto\n")
    while valor <= 0:
        print("El valor del producto no puede ser menor o igual a 0")
        valor = float(input("Digite el valor del producto\n"))
    while codigo <= 0:
        print("El codigo del producto no puede ser menor o igual a 0")
        codigo = int(input("Digite el codigo del producto que se añadira\n"))

    for producto in productos:
        if producto[0] == codigo:
            print("El codigo del producto ya existe, por favor ingrese un codigo diferente")
            return
    
    productos.append(list([codigo, nombre, valor]))
    guardarProductosArchivo(productos)

def listarProductos():
    if len(productos) == 0:
        print("No hay productos registrados, por favor agregue un producto para continuar")
    for producto in productos:
        print(f"Codigo: {producto[0]} | Nombre: {producto[1]} | Valor: {producto[2]}")

def eliminarProducto(): 
    codigo = int(input("Digite el codigo del producto que se eliminara\n"))
    for producto in productos:
        if producto[0] == codigo:
            productos.remove(producto)
            print("Producto eliminado exitosamente")
            guardarProductosArchivo(productos)
            return
    
    print("No se encontro el producto con el codigo especificado")

print("Bienvenido al Gestor de Productos")

while True:
    print("Analice las opciones y escoja apropiadamente \n")
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Listar todos los productos")
    print("3. Eliminar un producto")
    print("0. Salir")
    opcion = int(input("Escoja la opcion para gestionar\n"))
    if opcion == 1:
        agregarProducto()
        continue
    elif opcion == 2: 
        listarProductos()
        continue
    elif opcion == 3:
        eliminarProducto()
        continue
    else:
        break
    
            
