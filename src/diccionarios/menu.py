from src.datos.pizzas import pizzas
from src.datos.bebidas import bebidas
from src.carrito import (
    agregar_producto_carrito,
    eliminar_producto_carrito,
    mostrar_carrito,
)
from src.precios_integracion import calcular_precio_pizza
from src.costes_negocio.costes_negocio import prevision_ventas
from src.ofertas import aplicar_mejor_oferta
from src.ticket import mostrar_ticket


def mostrar_menu():
    print("\n================================")
    print("       PIZZERIA MARTINPAU")
    print("================================")
    print("1. Ver catalogo de pizzas")
    print("2. Ver catalogo de bebidas")
    print("3. Anadir pizza al carrito")
    print("4. Anadir bebida al carrito")
    print("5. Ver carrito")
    print("6. Eliminar producto")
    print("7. Consultar ofertas disponibles")
    print("8. Finalizar pedido")
    print("9. Salir")
    print("================================")


def seleccionar_temporada():
    opciones = {"1": "baja", "2": "media", "3": "alta"}
    while True:
        print("\nSelecciona la temporada de ventas:")
        print(f"1. Baja ({prevision_ventas['baja']['pizzas']} pizzas/mes)")
        print(f"2. Media ({prevision_ventas['media']['pizzas']} pizzas/mes)")
        print(f"3. Alta ({prevision_ventas['alta']['pizzas']} pizzas/mes)")
        opcion = input("Temporada [Enter = media]: ").strip().lower()

        if opcion == "":
            return "media"
        if opcion in opciones:
            return opciones[opcion]
        if opcion in opciones.values():
            return opcion
        print("Error: selecciona 1, 2 o 3.")


def mostrar_pizzas(temporada="media"):
    print("\n========== CARTA DE PIZZAS ==========")
    for numero, (nombre, ingredientes) in enumerate(pizzas.items(), 1):
        precio = calcular_precio_pizza(nombre, temporada)["precio_final"]
        nombres_ingredientes = [
            ingrediente.replace("_", " ") for ingrediente in ingredientes
        ]
        print(f"\n{numero}. {nombre.replace('_', ' ')} - {precio:.2f} EUR")
        print(f"   Ingredientes: {', '.join(nombres_ingredientes)}")
    print("\n=====================================")


def mostrar_bebidas():
    print("\n========== CARTA DE BEBIDAS ==========")
    for numero, (nombre, datos) in enumerate(bebidas.items(), 1):
        print(f"{numero}. {nombre} ({datos['formato']}) - "
              f"{datos['precio_venta']:.2f} EUR")
    print("======================================")


def mostrar_ofertas():
    print("\n========== OFERTAS DISPONIBLES ==========")
    print("1. Pizza + bebida: 1 EUR menos por cada pareja.")
    print("2. 2x1 Margarita: una gratis por cada dos.")
    print("3. 10% de descuento si el pedido supera 30 EUR.")
    print("Se aplica automaticamente solo la oferta mas ventajosa.")
    print("=========================================")


def seleccionar_pizza():
    nombres = list(pizzas.keys())
    print("\n========== ELEGIR PIZZA ==========")
    for numero, nombre in enumerate(nombres, 1):
        print(f"{numero}. {nombre.replace('_', ' ')}")

    opcion = input("Numero de pizza: ").strip()
    if not opcion.isdigit() or not 1 <= int(opcion) <= len(nombres):
        print("Error: numero de pizza no valido.")
        return None

    cantidad = input("Cuantas pizzas quieres?: ").strip()
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Error: cantidad no valida.")
        return None

    return nombres[int(opcion) - 1], int(cantidad)


def seleccionar_bebida():
    nombres = list(bebidas.keys())
    mostrar_bebidas()
    opcion = input("Numero de bebida: ").strip()
    if not opcion.isdigit() or not 1 <= int(opcion) <= len(nombres):
        print("Error: numero de bebida no valido.")
        return None

    cantidad = input("Cuantas bebidas quieres?: ").strip()
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Error: cantidad no valida.")
        return None

    return nombres[int(opcion) - 1], int(cantidad)


def quitar_del_carrito(carrito):
    if not carrito:
        print("El carrito esta vacio.")
        return

    mostrar_carrito(carrito)
    opcion = input("Numero del producto a eliminar: ").strip()
    if not opcion.isdigit() or not 1 <= int(opcion) <= len(carrito):
        print("Error: producto no valido.")
        return

    indice = int(opcion) - 1
    cantidad_actual = carrito[indice]["cantidad"]
    if cantidad_actual == 1:
        eliminar_producto_carrito(carrito, indice)
        return

    cantidad = input(f"Tienes {cantidad_actual}. Cuantas quieres quitar?: ").strip()
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Error: cantidad no valida.")
        return
    eliminar_producto_carrito(carrito, indice, int(cantidad))


def iniciar_menu():
    carrito = []
    temporada = seleccionar_temporada()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            mostrar_pizzas(temporada)

        elif opcion == "2":
            mostrar_bebidas()

        elif opcion == "3":
            seleccion = seleccionar_pizza()
            if seleccion is not None:
                nombre, cantidad = seleccion
                precio = calcular_precio_pizza(nombre, temporada)["precio_final"]
                agregar_producto_carrito(carrito, nombre, cantidad, precio)
                print(f"Anadidas {cantidad} x {nombre.replace('_', ' ')} "
                      f"a {precio:.2f} EUR cada una.")

        elif opcion == "4":
            seleccion = seleccionar_bebida()
            if seleccion is not None:
                nombre, cantidad = seleccion
                precio = bebidas[nombre]["precio_venta"]
                agregar_producto_carrito(carrito, nombre, cantidad, precio)
                print(f"Anadidas {cantidad} x {nombre} "
                      f"a {precio:.2f} EUR cada una.")

        elif opcion == "5":
            mostrar_carrito(carrito)

        elif opcion == "6":
            quitar_del_carrito(carrito)

        elif opcion == "7":
            mostrar_ofertas()

        elif opcion == "8":
            if not carrito:
                print("No puedes finalizar un pedido vacio.")
            else:
                nombre_oferta, descuento, _ = aplicar_mejor_oferta(
                    carrito, list(pizzas.keys()), list(bebidas.keys())
                )
                mostrar_ticket(carrito, descuento, nombre_oferta)
                carrito.clear()

        elif opcion == "9":
            print("Gracias por utilizar Pizzeria MartinPau!")
            break

        else:
            print("Opcion no valida. Intentalo de nuevo.")


if __name__ == "__main__":
    iniciar_menu()
