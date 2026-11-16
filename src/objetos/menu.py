from src.carrito import (
    agregar_producto_carrito,
    eliminar_producto_carrito,
    mostrar_carrito,
)
from src.costes_negocio.costes_negocio import prevision_ventas
from src.datos.bebidas import bebidas
from src.datos.pizzas import pizzas
from src.ofertas import aplicar_mejor_oferta
from src.precios_integracion import calcular_precio_pizza
from src.ticket import mostrar_ticket


class PizzaObjeto:
    def __init__(self, nombre, ingredientes, precio):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio

    def mostrar(self):
        return f"{self.nombre.replace('_', ' ')} - {self.precio:.2f} EUR"


class BebidaObjeto:
    def __init__(self, nombre, formato, precio):
        self.nombre = nombre
        self.formato = formato
        self.precio = precio

    def mostrar(self):
        return f"{self.nombre} ({self.formato}) - {self.precio:.2f} EUR"


class CatalogoPizzas:
    def __init__(self):
        self.items = []
        for nombre, ingredientes in pizzas.items():
            precio = calcular_precio_pizza(nombre, "media")["precio_final"]
            self.items.append(PizzaObjeto(nombre, ingredientes, precio))

    def mostrar(self):
        for i, pizza in enumerate(self.items, 1):
            print(f"{i}. {pizza.mostrar()}")

    def obtener_por_indice(self, indice):
        return self.items[indice]


class CatalogoBebidas:
    def __init__(self):
        self.items = []
        for nombre, datos in bebidas.items():
            self.items.append(
                BebidaObjeto(nombre, datos["formato"], datos["precio_venta"])
            )

    def mostrar(self):
        for i, bebida in enumerate(self.items, 1):
            print(f"{i}. {bebida.mostrar()}")

    def obtener_por_indice(self, indice):
        return self.items[indice]


class MenuObjetos:
    def __init__(self):
        self.catalogo_pizzas = CatalogoPizzas()
        self.catalogo_bebidas = CatalogoBebidas()

    def mostrar_menu(self):
        print("\n================================")
        print("      PIZZERIA MARTINPAU (OBJETOS)")
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

    def seleccionar_temporada(self):
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

    def seleccionar_pizza(self):
        self.catalogo_pizzas.mostrar()
        opcion = input("Numero de pizza: ").strip()
        if not opcion.isdigit() or not 1 <= int(opcion) <= len(self.catalogo_pizzas.items):
            print("Error: numero de pizza no valido.")
            return None

        cantidad = input("Cuantas pizzas quieres?: ").strip()
        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Error: cantidad no valida.")
            return None

        pizza = self.catalogo_pizzas.obtener_por_indice(int(opcion) - 1)
        return pizza, int(cantidad)

    def seleccionar_bebida(self):
        self.catalogo_bebidas.mostrar()
        opcion = input("Numero de bebida: ").strip()
        if not opcion.isdigit() or not 1 <= int(opcion) <= len(self.catalogo_bebidas.items):
            print("Error: numero de bebida no valido.")
            return None

        cantidad = input("Cuantas bebidas quieres?: ").strip()
        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Error: cantidad no valida.")
            return None

        bebida = self.catalogo_bebidas.obtener_por_indice(int(opcion) - 1)
        return bebida, int(cantidad)

    def quitar_del_carrito(self, carrito):
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

    def iniciar_menu(self):
        carrito = []
        temporada = self.seleccionar_temporada()

        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opcion: ").strip()

            if opcion == "1":
                self.catalogo_pizzas.mostrar()

            elif opcion == "2":
                self.catalogo_bebidas.mostrar()

            elif opcion == "3":
                seleccion = self.seleccionar_pizza()
                if seleccion is not None:
                    pizza, cantidad = seleccion
                    precio = calcular_precio_pizza(pizza.nombre, temporada)["precio_final"]
                    agregar_producto_carrito(carrito, pizza.nombre, cantidad, precio)
                    print(
                        f"Anadidas {cantidad} x {pizza.nombre.replace('_', ' ')} "
                        f"a {precio:.2f} EUR cada una."
                    )

            elif opcion == "4":
                seleccion = self.seleccionar_bebida()
                if seleccion is not None:
                    bebida, cantidad = seleccion
                    agregar_producto_carrito(carrito, bebida.nombre, cantidad, bebida.precio)
                    print(
                        f"Anadidas {cantidad} x {bebida.nombre} "
                        f"a {bebida.precio:.2f} EUR cada una."
                    )

            elif opcion == "5":
                mostrar_carrito(carrito)

            elif opcion == "6":
                self.quitar_del_carrito(carrito)

            elif opcion == "7":
                print("\n========== OFERTAS DISPONIBLES ==========")
                print("1. Pizza + bebida: 1 EUR menos por cada pareja.")
                print("2. 2x1 Margarita: una gratis por cada dos.")
                print("3. 10% de descuento si el pedido supera 30 EUR.")
                print("Se aplica automaticamente solo la oferta mas ventajosa.")
                print("=========================================")

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
                print("Gracias por utilizar Pizzeria MartinPau! (version objetos)")
                break

            else:
                print("Opcion no valida. Intentalo de nuevo.")


def iniciar_menu():
    MenuObjetos().iniciar_menu()


if __name__ == "__main__":
    iniciar_menu()
