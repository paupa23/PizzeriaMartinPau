class Pizza:
    # Constructor de la clase
    # Recibe el nombre, los ingredientes de la receta
    # y el catálogo de ingredientes
    def __init__(self, nombre, ingredientes, catalogo_ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.catalogo_ingredientes = catalogo_ingredientes

    # Calcula el coste total de la pizza
    def calcular_coste(self):

        # Inicializamos el coste total
        coste_total = 0

        # Recorremos los ingredientes de la receta
        for nombre_ingrediente, cantidad in self.ingredientes.items():

            # Buscamos el objeto Ingrediente en el catálogo
            ingrediente = self.catalogo_ingredientes.obtener_ingrediente(
                nombre_ingrediente
            )

            # Calculamos el coste de la cantidad utilizada
            coste = ingrediente.calcular_coste(cantidad)

            # Sumamos el coste al total
            coste_total += coste

        # Devolvemos el coste total de la pizza
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
        def cargar_pizzas(self, recetas, catalogo_ingredientes):
    
            # Recorremos todas las recetas
            for nombre, ingredientes in recetas.items():
    
                # Creamos un objeto Pizza con la receta
                pizza = Pizza(
                    nombre,
                    ingredientes,
                    catalogo_ingredientes
                )
    
                # Añadimos la pizza al catálogo
                self.agregar_pizza(pizza)
        
def crear_catalogo_pizzas(catalogo_ingredientes):

    # Importamos las recetas del proyecto original
    from src.datos.pizzas import pizzas as recetas

    # Creamos el catálogo de pizzas
    catalogo = CatalogoPizzas()

    # Cargamos todas las recetas originales
    catalogo.cargar_pizzas(
        recetas,
        catalogo_ingredientes
    )

    # Devolvemos el catálogo
    return catalogo