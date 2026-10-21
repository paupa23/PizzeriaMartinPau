from src.carrito import calcular_total_carrito

def mostrar_ticket(carrito, descuento=0, nombre_oferta="Sin oferta"):

    print("\n================================")
    print("       PIZZERIA MARTINPAU")
    print("================================")
    print("         TICKET DE COMPRA")
    print("--------------------------------")

    if len(carrito) == 0:
        print("El carrito esta vacio.")
        return

    for item in carrito:
        producto = item["producto"]
        cantidad = item["cantidad"]
        precio = item["precio"]

        subtotal = cantidad * precio

        print(f"{cantidad} x {producto}")
        print(f"    {precio:.2f} EUR/u = {subtotal:.2f} EUR")

    print("--------------------------------")
    
    # Calcular el subtotal del pedido
    subtotal = calcular_total_carrito(carrito)

    print(f"Subtotal: {subtotal:.2f} EUR")

    # Comprobar que el descuento sea válido
    descuento = max(0, min(descuento, subtotal))

    # Mostrar la oferta aplicada
    if descuento > 0:
        print(f"Oferta aplicada: {nombre_oferta}")
        print(f"Descuento: -{descuento:.2f} EUR")
    else:
        print("Sin descuentos aplicados.")

    # Calcular el total después del descuento
    total_con_descuento = round(subtotal - descuento, 2)

    print("--------------------------------")
    print(f"Total con descuento: {total_con_descuento:.2f} EUR")
    
    # Calcular la base imponible sin IVA
    iva_porcentaje = 0.10

    base_imponible = round(
        total_con_descuento / (1 + iva_porcentaje), 2
    )

    # Calcular el IVA incluido en el precio
    importe_iva = round(
        total_con_descuento - base_imponible, 2
    )

    # Mostrar el desglose del IVA
    print("--------------------------------")
    print(f"Base imponible: {base_imponible:.2f} EUR")
    print(f"IVA (10%): {importe_iva:.2f} EUR")
    
    # Mostrar el total final del pedido
    print("================================")
    print(f"TOTAL A PAGAR: {total_con_descuento:.2f} EUR")
    print("================================")

    # Mensaje de agradecimiento
    print("Gracias por comprar en Pizzeria MartinPau!")
    print("Esperamos verte pronto!")
    print("================================")



