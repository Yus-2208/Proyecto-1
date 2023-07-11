# Definicion de variables
almacen = {'harina': 20, 'arroz': 16, 'pasta': 28, 'leche': 49, 'azucar': 32, 'sal': 19} # Diccionario para almacenar el stock de productos
inventario = {'harina': 1.2, 'arroz': 1.5, 'pasta': 1.4, 'leche': 2.4, 'azucar': 2.1, 'sal': 0.75}  # Diccionario para almacenar los precios de los productos
lista_de_compras = []  # Lista para almacenar los productos comprados
suma_total = 0  # Variable para almacenar el total de la compra
factura = {} #Diccionario para almacenar el nombre del producto con el monto

# Ciclo de repeticion
while True:
    # Menu de opciones
    print("---- Tienda ----")
    print("1. Ver productos disponibles")
    print("2. Agregar producto al inventario")
    print("3. Realizar una compra")
    print("4. Calcular el total de la compra")
    print("5. Salir del programa")
    opcion = int(input("Ingrese el numero de la opcion que desee: "))

    if  opcion == 1:
        #Ver los productos disponibles en el almacen
        print("Los productos disponibles son: ", 
              almacen)
    
    elif opcion == 2:
        # Agregar producto al inventario
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: ")) #$

        almacen[producto] = cantidad  # Guardar cantidad en el diccionario almacen
        inventario[producto] = precio  # Guardar precio en el diccionario inventario
    elif opcion == 3:
        # Realizar una compra
        nombre_del_producto = input("Ingrese el producto a comprar: ")
        cantidad_del_producto = int(input("Ingrese la cantidad del producto a comprar: "))

        if cantidad_del_producto <= 0:
            print("La cantidad del producto debe ser mayor a 0")
        elif nombre_del_producto not in almacen:
            print("El producto ingresado no esta en el inventario")
        elif almacen[nombre_del_producto] < cantidad_del_producto:
            print("Lo sentimos, no tenemos la cantidad que desea. Solo tenemos", almacen[nombre_del_producto])
        else:
            # Procesar la compra
            valor_1 = almacen[nombre_del_producto] - cantidad_del_producto
            almacen[nombre_del_producto] = valor_1
            valor = cantidad_del_producto * inventario[nombre_del_producto]
            lista_de_compras.append(valor)  # Agregar el valor a la lista de compras
            factura[nombre_del_producto] = valor #Agregar el producto que se esta comprando con el monto a un diccionario
    elif opcion == 4:
        # Calcular el total de la compra
        total = 0
        for producto in lista_de_compras:
            total += producto  # Sumar el valor de cada producto a total
        print("su factura es: ",factura )
        print("El total de la compra es:", total) #$
    elif opcion == 5:
        # Salir del programa
        break
    else:
        print("Opcion invalida. Por favor, ingrese un numero valido.")

print("Gracias por entrar a la tienda ")