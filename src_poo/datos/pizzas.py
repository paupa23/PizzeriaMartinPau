from src_poo.costes_negocio.precios_ingredientes import peso_unidad_g

class Pizza:
    # Constructor de la clase
    # Recibe el nombre, los ingredientes de la receta
    # y el catálogo de ingredientes
    # Constructor de la clase
    def __init__(
        self,
        nombre,
        ingredientes,
        catalogo_ingredientes,
        unidades_ingredientes
    ):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.catalogo_ingredientes = catalogo_ingredientes
        self.unidades_ingredientes = unidades_ingredientes

        # Calcula el coste total de la pizza
    # Calcula el coste total de la pizza
def calcular_coste(self):

    # Inicializamos el coste total
    coste_total = 0

    # Obtenemos las unidades específicas de esta pizza
    unidades_pizza = self.unidades_ingredientes.get(
        self.nombre,
        {}
    )

    # Recorremos los ingredientes de la receta
    for nombre_ingrediente, cantidad in self.ingredientes.items():

            # La masa tiene un cálculo especial
            if nombre_ingrediente == "masa":

                # Calculamos el coste de la masa
                coste = self.catalogo_ingredientes.calcular_coste_masa()

            # La mezcla de quesos tiene un cálculo especial
            elif nombre_ingrediente == "mezcla_quesos":

                # Calculamos el precio medio de los quesos
                precio_medio = (
                    self.catalogo_ingredientes
                    .calcular_coste_mezcla_quesos()
                )

                # La cantidad de la receta está expresada en gramos
                coste = precio_medio * (cantidad / 1000)

            else:

                # Buscamos el objeto Ingrediente
                ingrediente = self.catalogo_ingredientes.obtener_ingrediente(
                    nombre_ingrediente
                )

                # Obtenemos la unidad de la receta
                unidad_receta = unidades_pizza.get(
                    nombre_ingrediente,
                    "g"
                )

                # Obtenemos el peso por unidad si existe
                peso_unidad = peso_unidad_g.get(
                    nombre_ingrediente
                )

                # Calculamos el coste del ingrediente
                coste = ingrediente.calcular_coste(
                    cantidad,
                    unidad_receta,
                    peso_unidad
                )

            # Sumamos el coste al total
            coste_total += coste

    # Devolvemos el coste total
    return coste_total

class CatalogoPizzas:

    # Constructor de la clase
    def __init__(self):
        self.pizzas = {}
    
    # Añade una pizza al catálogo
        def agregar_pizza(self, pizza):
            self.pizzas[pizza.nombre] = pizza
    
        # Busca una pizza por su nombre
        def obtener_pizza(self, nombre):
            if nombre not in self.pizzas:
                raise ValueError(f"No existe la pizza: {nombre}")
    
            return self.pizzas[nombre]
            
            # Carga las pizzas a partir de un diccionario de recetas
    def cargar_pizzas(
        self,
        recetas,
        catalogo_ingredientes,
        unidades_ingredientes
    ):

        # Recorremos todas las recetas
        for nombre, ingredientes in recetas.items():

            # Creamos un objeto Pizza con la receta
            pizza = Pizza(
                nombre,
                ingredientes,
                catalogo_ingredientes,
                unidades_ingredientes
            )

            # Añadimos la pizza al catálogo
            self.agregar_pizza(pizza)
        
def crear_catalogo_pizzas(catalogo_ingredientes):

    # Importamos las recetas del proyecto original
    from src.datos.pizzas import pizzas as recetas

    # Importamos las unidades de los ingredientes
    from src.datos.ingredientes import unidades_ingredientes

    # Creamos el catálogo de pizzas
    catalogo = CatalogoPizzas()

    # Cargamos todas las recetas originales
    catalogo.cargar_pizzas(
        recetas,
        catalogo_ingredientes,
        unidades_ingredientes
    )

    # Devolvemos el catálogo
    return catalogo