from src.carrito import calcular_total_carrito

def oferta_pizza_bebida(carrito, nombres_pizzas, nombres_bebidas):
    cantidad_pizzas = 0
    cantidad_bebidas = 0

    for item in carrito:
        producto = item["producto"]
        cantidad = item["cantidad"]

        if producto in nombres_pizzas:
            cantidad_pizzas += cantidad

        elif producto in nombres_bebidas:
            cantidad_bebidas += cantidad

    menus = min(cantidad_pizzas, cantidad_bebidas)

    descuento = menus * 1.00

    return descuento



def oferta_dos_por_uno(carrito):
    cantidad_margaritas = 0
    precio_margarita = 0

    for item in carrito:
        if item["producto"] == "Margarita":
            cantidad_margaritas += item["cantidad"]
            precio_margarita = item["precio"]

    pizzas_gratis = cantidad_margaritas // 2

    descuento = pizzas_gratis * precio_margarita

    return round(descuento, 2)



def oferta_descuento_diez_por_ciento(carrito):
    total = calcular_total_carrito(carrito)

    if total > 30:
        descuento = total * 0.10
    else:
        descuento = 0

    return round(descuento, 2)



def aplicar_oferta(carrito, tipo_oferta, nombres_pizzas, nombres_bebidas):

    if tipo_oferta == 1:
        descuento = oferta_pizza_bebida(
            carrito, nombres_pizzas, nombres_bebidas
        )

    elif tipo_oferta == 2:
        descuento = oferta_dos_por_uno(carrito)

    elif tipo_oferta == 3:
        descuento = oferta_descuento_diez_por_ciento(carrito)

    else:
        print("Oferta no válida.")
        descuento = 0

    total_carrito = calcular_total_carrito(carrito)

    descuento = min(descuento, total_carrito)
    total_final = round(total_carrito - descuento, 2)

    return round(descuento, 2), total_final
