from src_poo.datos.ingredientes import Ingrediente

# Lista de quesos que forman la mezcla
quesos_mezcla = [
    "mozzarella",
    "cheddar",
    "gouda",
    "queso_azul",
    "parmesano",
    "queso_suave",
    "emmental",
    "havarti",
]

class CatalogoIngredientes:
    def __init__(self):
        self.ingredientes = {}

    def agregar_ingredientes(self,nombre,precio,unidad):
        # Creamos un objeto de la clase Ingrediente con los datos recibidos
        ingrediente = Ingrediente(nombre,precio,unidad)
        # Guardamos ese objeto en el diccionario self.ingredientes, utilizando su nombre como clave.
        self.ingredientes[nombre] = ingrediente

def crear_catalogo_ingredientes(self):
    catalogo = CatalogoIngredientes()

    # Ingredientes para la masa
    catalogo.agregar_ingrediente("harina", 0.72, "kg")
    catalogo.agregar_ingrediente("agua", 0.33, "l")
    catalogo.agregar_ingrediente("aceite", 3.70, "l")
    catalogo.agregar_ingrediente("levadura", 10.00, "kg")
    catalogo.agregar_ingrediente("sal", 0.40, "kg")

    # Quesos
    catalogo.agregar_ingrediente("mozzarella", 8.00, "kg")
    catalogo.agregar_ingrediente("cheddar", 9.75, "kg")
    catalogo.agregar_ingrediente("gouda", 6.50, "kg")
    catalogo.agregar_ingrediente("queso_azul", 12.78, "kg")
    catalogo.agregar_ingrediente("parmesano", 16.50, "kg")
    catalogo.agregar_ingrediente("queso_suave", 7.64, "kg")
    catalogo.agregar_ingrediente("emmental", 6.37, "kg")
    catalogo.agregar_ingrediente("havarti", 9.33, "kg")

    # Lácteos
    catalogo.agregar_ingrediente("nata", 3.08, "l")

    # Carnes
    catalogo.agregar_ingrediente("jamon_cocido", 11.25, "kg")
    catalogo.agregar_ingrediente("bacon", 9.20, "kg")
    catalogo.agregar_ingrediente("panceta_italiana", 15.00, "kg")
    catalogo.agregar_ingrediente("pechuga_pollo", 7.70, "kg")
    catalogo.agregar_ingrediente("pollo_marinado", 8.20, "kg")
    catalogo.agregar_ingrediente("carne_picada_vacuno", 11.00, "kg")
    catalogo.agregar_ingrediente("carne_picada_mixta", 8.20, "kg")
    catalogo.agregar_ingrediente("pepperoni", 21.33, "kg")

    # Verduras y hortalizas
    catalogo.agregar_ingrediente("cebolla_blanca", 1.50, "kg")
    catalogo.agregar_ingrediente("cebolla_morada", 1.40, "kg")
    catalogo.agregar_ingrediente("champiñones", 5.56, "kg")
    catalogo.agregar_ingrediente("alcachofa", 2.53, "kg")
    catalogo.agregar_ingrediente("pimiento_rojo", 2.89, "kg")
    catalogo.agregar_ingrediente("pimiento_verde", 2.80, "kg")
    catalogo.agregar_ingrediente("tomates_cherry", 4.40, "kg")
    catalogo.agregar_ingrediente("berenjena", 2.20, "kg")
    catalogo.agregar_ingrediente("rucula", 17.00, "kg")
    catalogo.agregar_ingrediente("ajo", 7.40, "kg")
    catalogo.agregar_ingrediente("piña", 2.00, "kg")
    catalogo.agregar_ingrediente("albahaca", 77.50, "kg")
    catalogo.agregar_ingrediente("perejil", 23.75, "kg")
    catalogo.agregar_ingrediente("oregano", 40.00, "kg")

    # Pescados y mariscos
    catalogo.agregar_ingrediente("gambas", 13.61, "kg")
    catalogo.agregar_ingrediente("calamar", 15.97, "kg")
    catalogo.agregar_ingrediente("mejillones", 9.09, "kg")
    catalogo.agregar_ingrediente("anchoas", 17.50, "kg")

    # Salsas y condimentos
    catalogo.agregar_ingrediente("salsa_tomate", 1.25, "kg")
    catalogo.agregar_ingrediente("salsa_barbacoa", 3.29, "kg")
    catalogo.agregar_ingrediente("salsa_burger", 5.60, "l")
    catalogo.agregar_ingrediente("salsa_kebab", 4.03, "l")
    catalogo.agregar_ingrediente("salsa_pesto", 12.67, "kg")
    catalogo.agregar_ingrediente("vinagre", 4.60, "l")
    catalogo.agregar_ingrediente("pimienta", 18.57, "kg")
    catalogo.agregar_ingrediente("especias_kebab", 24.19, "kg")
    catalogo.agregar_ingrediente("olivas_negras", 12.84, "kg")
    catalogo.agregar_ingrediente("alcaparras", 10.00, "kg")
    catalogo.agregar_ingrediente("piñones", 50.71, "kg")

    # Otros ingredientes
    catalogo.agregar_ingrediente("huevo", 0.24, "unidad")
    catalogo.agregar_ingrediente("bolsa_cheetos", 1.89, "unidad")

    return catalogo

class CatalogoIngredientes:

    # Constructor de la clase
    def __init__(self):
        self.ingredientes = {}

    # Añade un ingrediente al catálogo
    def agregar_ingrediente(self, nombre, precio, unidad):
        ingrediente = Ingrediente(nombre, precio, unidad)
        self.ingredientes[nombre] = ingrediente

    # Busca un ingrediente por su nombre
    def obtener_ingrediente(self, nombre):

        # Comprobamos si el ingrediente existe en el catálogo
        if nombre not in self.ingredientes:
            raise ValueError(f"No existe el ingrediente: {nombre}")

        # Devolvemos el objeto Ingrediente
        return self.ingredientes[nombre]

        # Calcula el coste de la masa utilizada en una pizza
    def calcular_coste_masa(self):

        # Coste de 250 g de harina
        coste_harina = self.obtener_ingrediente(
            "harina"
        ).calcular_coste(250, "g")

        # Coste de 160 ml de agua
        coste_agua = self.obtener_ingrediente(
            "agua"
        ).calcular_coste(160, "ml")

        # Coste de 25 ml de aceite
        coste_aceite = self.obtener_ingrediente(
            "aceite"
        ).calcular_coste(25, "ml")

        # Coste de 10 g de levadura
        coste_levadura = self.obtener_ingrediente(
            "levadura"
        ).calcular_coste(10, "g")

        # Coste de 4 g de sal
        coste_sal = self.obtener_ingrediente(
            "sal"
        ).calcular_coste(4, "g")

        # Calculamos el coste total de la receta de masa
        coste_total = (
            coste_harina
            + coste_agua
            + coste_aceite
            + coste_levadura
            + coste_sal
        )

        # La receta completa produce aproximadamente 449 g de masa
        # Cada pizza utiliza 220 g
        coste_pizza = coste_total * (220 / 449)

        # Devolvemos el coste de la masa de una pizza
        return coste_pizza

    # Calcula el precio medio de la mezcla de quesos
    def calcular_coste_mezcla_quesos(self):

        # Inicializamos el coste total
        coste_total = 0

        # Recorremos todos los quesos de la mezcla
        for nombre_queso in quesos_mezcla:

            # Obtenemos el queso del catálogo
            queso = self.obtener_ingrediente(nombre_queso)

            # Sumamos su precio
            coste_total += queso.precio

        # Calculamos el precio medio
        return coste_total / len(quesos_mezcla)