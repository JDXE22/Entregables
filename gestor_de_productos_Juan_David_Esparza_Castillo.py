productos = []

def agregarProducto():
    codigo = int(input("Digite el codigo del producto que se añadira\n"))
    nombre = input("Digite el nombre del producto\n")
    valor = float(input("Digite el valor del producto\n"))
    while len(nombre) == 0:
        print("El nombre del producto no puede estar vacio")
        nombre = input("Digite el nombre del producto\n")

    productos_a_agregar = [codigo,nombre,valor]
    productos.append(productos_a_agregar)

def listarProductos():
     print(productos)

def eliminarProducto(): 
    codigo = int(input("Digite el codigo del producto que se eliminara\n"))
    for producto in productos:
        if producto[0] == codigo:
            productos.remove(producto)
            print("Producto eliminado exitosamente")
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
    
            
