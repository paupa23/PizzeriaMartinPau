def agregar_producto_carrito(carrito, producto, cantidad, precio):
    item = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio
    }

    carrito.append(item)
    return carrito


def eliminar_producto_carrito(carrito, indice):
    if 0 <= indice < len(carrito):
        carrito.pop(indice)
        print("Producto eliminado correctamente.")
    else:
        print("Error: el producto no existe.")

    return carrito


def mostrar_carrito(carrito):
    if len(carrito) == 0:
        print("El carrito está vacío.")
        return

    print("\n===== CARRITO DE COMPRA =====")

    for indice, item in enumerate(carrito):
        producto = item["producto"]
        cantidad = item["cantidad"]
        precio = item["precio"]
        subtotal = cantidad * precio

        print(f"{indice + 1}. {producto}")
        print(f"   Cantidad: {cantidad}")
        print(f"   Precio unitario: {precio:.2f} €")
        print(f"   Subtotal: {subtotal:.2f} €")

    print("============================")


def calcular_total_carrito(carrito):
    total = 0

    for item in carrito:
        cantidad = item["cantidad"]
        precio = item["precio"]

        subtotal = cantidad * precio
        total += subtotal

    return round(total, 2)