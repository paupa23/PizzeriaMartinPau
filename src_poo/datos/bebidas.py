class Bebida:

    # Constructor de la clase
    def __init__(self, nombre, formato, precio_venta):
        self.nombre = nombre
        self.formato = formato
        self.precio_venta = precio_venta


class CatalogoBebidas:

    # Constructor de la clase
    def __init__(self):
        self.bebidas = {}

    # Añade una bebida al catálogo
    def agregar_bebida(self, bebida):
        self.bebidas[bebida.nombre] = bebida

    # Busca una bebida por su nombre
    def obtener_bebida(self, nombre):
        if nombre not in self.bebidas:
            raise ValueError(f"No existe la bebida: {nombre}")

        return self.bebidas[nombre]

    # Carga las bebidas a partir de un diccionario
    def cargar_bebidas(self, bebidas_originales):

        # Recorremos todas las bebidas
        for nombre, datos in bebidas_originales.items():

            # Creamos el objeto Bebida
            bebida = Bebida(
                nombre,
                datos["formato"],
                datos["precio_venta"]
            )

            # Añadimos la bebida al catálogo
            self.agregar_bebida(bebida)


def crear_catalogo_bebidas():

    # Importamos las bebidas del proyecto original
    from src.datos.bebidas import bebidas as bebidas_originales

    # Creamos el catálogo
    catalogo = CatalogoBebidas()

    # Cargamos las bebidas originales
    catalogo.cargar_bebidas(bebidas_originales)

    # Devolvemos el catálogo
    return catalogo