from src.datos import pizzas
from src.carrito import (
    mostrar_carrito,
    agregar_producto_carrito,
    eliminar_producto_carrito
)
from src.ofertas import aplicar_mejor_oferta
from src.ticket import mostrar_ticket


# Mostrar el menu principal
def mostrar_menu():
    print("\n================================")
    print("       PIZZERIA MARTINPAU")
    print("================================")
    print("1. Ver catalogo de pizzas")
    print("2. Ver catalogo de bebidas")
    print("3. Añadir pizza al carrito")
    print("4. Añadir bebida al carrito")
    print("5. Ver carrito")
    print("6. Eliminar producto")
    print("7. Consultar ofertas disponibles")
    print("8. Finalizar pedido")
    print("9. Salir")
    print("================================")


# Mostrar todas las pizzas y sus ingredientes
def mostrar_pizzas():
    print("\n========== CARTA DE PIZZAS ==========")

    for numero, (nombre, ingredientes) in enumerate(pizzas.items(), 1):
        nombre_mostrar = nombre.replace("_", " ")

        ingredientes_mostrar = [
            ingrediente.replace("_", " ")
            for ingrediente in ingredientes.keys()
        ]

        print(f"\n{numero}. {nombre_mostrar}")
        print(f"   Ingredientes: {', '.join(ingredientes_mostrar)}")

    print("\n=====================================")



# Mostrar las ofertas disponibles
def mostrar_ofertas():
    print("\n================================")
    print("       OFERTAS DISPONIBLES")
    print("================================")

    print("\n1. MENU PIZZA + BEBIDA")
    print("   Descuento de 1 EUR por cada")
    print("   combinacion de pizza y bebida.")

    print("\n2. OFERTA 2X1 MARGARITA")
    print("   Por cada 2 pizzas Margarita,")
    print("   una de ellas es gratis.")

    print("\n3. DESCUENTO DEL 10%")
    print("   En pedidos superiores a 30 EUR")
    print("   se aplica un 10% de descuento.")

    print("\n================================")
    print("Las ofertas se aplican automaticamente.")
    print("Siempre se elige la de mayor descuento.")
    print("Las promociones no son acumulables.")
    print("================================")



# Permitir al cliente seleccionar una pizza
def seleccionar_pizza():
    print("\n========== ELEGIR PIZZA ==========")

    nombres_pizzas = list(pizzas.keys())

    for numero, nombre in enumerate(nombres_pizzas, 1):
        print(f"{numero}. {nombre.replace('_', ' ')}")

    print("==================================")

    opcion = input("Introduce el numero de la pizza: ").strip()

    if not opcion.isdigit():
        print("Error: debes introducir un numero.")
        return None

    numero = int(opcion)

    if numero < 1 or numero > len(nombres_pizzas):
        print("Error: esa pizza no existe.")
        return None

    pizza_elegida = nombres_pizzas[numero - 1]

    cantidad = input("Cuantas pizzas quieres?: ").strip()

    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Error: cantidad no valida.")
        return None

    cantidad = int(cantidad)

    print(f"\nHas seleccionado {cantidad} x {pizza_elegida.replace('_', ' ')}")

    return pizza_elegida, cantidad


# Iniciar el menu interactivo
def iniciar_menu():
    carrito = []

    while True:
        mostrar_menu()

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            mostrar_pizzas()

        elif opcion == "2":
            print("Has seleccionado: Ver bebidas")

        
        elif opcion == "3":
            seleccion = seleccionar_pizza()

            if seleccion is not None:
                pizza_elegida, cantidad = seleccion

                # Precio temporal para probar el carrito
                precio = 9.0

                agregar_producto_carrito(
                    carrito,
                    pizza_elegida,
                    cantidad,
                    precio
                )

                print("\nPizza añadida correctamente al carrito.")
                print(f"Pizza: {pizza_elegida.replace('_', ' ')}")
                print(f"Cantidad: {cantidad}")


        elif opcion == "4":
            print("Has seleccionado: Añadir bebida")

        elif opcion == "5":
            mostrar_carrito(carrito)

        
        
        elif opcion == "6":

            if len(carrito) == 0:
                print("\nEl carrito esta vacio.")

            else:
                mostrar_carrito(carrito)

                opcion_eliminar = input(
                    "\nIntroduce el numero del producto a eliminar: "
                ).strip()

                if not opcion_eliminar.isdigit():
                    print("Error: debes introducir un numero.")

                else:
                    indice = int(opcion_eliminar) - 1

                    if indice < 0 or indice >= len(carrito):
                        print("Error: el producto no existe.")

                    else:
                        cantidad_actual = carrito[indice]["cantidad"]

                        if cantidad_actual == 1:
                            eliminar_producto_carrito(carrito, indice)

                        else:
                            print(f"Tienes {cantidad_actual} unidades.")

                            cantidad_eliminar = input(
                                "Cuantas unidades quieres eliminar?: "
                            ).strip()

                            if not cantidad_eliminar.isdigit():
                                print("Error: cantidad no valida.")

                            else:
                                cantidad_eliminar = int(cantidad_eliminar)

                                eliminar_producto_carrito(
                                    carrito,
                                    indice,
                                    cantidad_eliminar
                                )


        elif opcion == "7":
            mostrar_ofertas()

        
        elif opcion == "8":

            if len(carrito) == 0:
                print("\nNo puedes finalizar un pedido vacio.")

            else:
                # Obtener los nombres de las pizzas
                nombres_pizzas = list(pizzas.keys())

                # Pendiente de conectar las bebidas
                nombres_bebidas = []

                # Buscar automaticamente la mejor oferta
                nombre_oferta, descuento, total = aplicar_mejor_oferta(
                    carrito,
                    nombres_pizzas,
                    nombres_bebidas
                )

                # Mostrar el ticket con la oferta aplicada
                mostrar_ticket(
                    carrito,
                    descuento,
                    nombre_oferta
                )

                # Vaciar el carrito para el siguiente cliente
                carrito.clear()


        elif opcion == "9":
            print("Gracias por utilizar Pizzeria MartinPau!")
            break

        else:
            print("Opcion no valida. Intentalo de nuevo.")


# Ejecutar el menu solo al iniciar este archivo directamente
if __name__ == "__main__":
    iniciar_menu()
