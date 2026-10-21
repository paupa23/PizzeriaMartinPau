from datos import pizzas, ingredientes
def calcular_coste_ingredientes(ingredientes, cantidad, precios_ingredientes):
    coste_total = 0

    for ingrediente in ingredientes:
        coste_total += precios_ingredientes[ingrediente] * cantidad[ingrediente]

    return coste_total    
