def agregar_producto_carrito(carrito, producto, cantidad, precio):
    item = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio
    }

    carrito.append(item)
    return carrito



def eliminar_producto_carrito(carrito, indice, cantidad=None):

    if indice < 0 or indice >= len(carrito):
        print("Error: el producto no existe.")
        return carrito

    producto = carrito[indice]
    cantidad_actual = producto["cantidad"]

    # Si no indicamos cantidad, eliminar todo el producto
    if cantidad is None:
        carrito.pop(indice)
        print("Producto eliminado correctamente.")
        return carrito

    # Comprobar que la cantidad sea valida
    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor que 0.")

    elif cantidad > cantidad_actual:
        print("Error: no tienes tantas unidades en el carrito.")

    elif cantidad == cantidad_actual:
        carrito.pop(indice)
        print("Producto eliminado completamente.")

    else:
        producto["cantidad"] -= cantidad
        print(f"Se han eliminado {cantidad} unidades.")
        print(f"Quedan {producto['cantidad']} unidades.")

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