class PreciosBebidas:

    # Constructor de la clase
    def __init__(self, catalogo_bebidas):
        self.catalogo_bebidas = catalogo_bebidas

    # Calcula el precio de venta por litro de todas las bebidas
    def calcular_precios_venta_litro(self):

        # Creamos un diccionario para guardar los resultados
        precios_venta_litro = {}

        # Recorremos todas las bebidas del catálogo
        for nombre, bebida in self.catalogo_bebidas.bebidas.items():

            # Obtenemos el precio de venta de la bebida
            precio_venta = bebida.precio_venta

            # Extraemos el volumen del formato
            volumen_ml = float(
                bebida.formato.replace(" ml", "")
            )

            # Convertimos los mililitros a litros
            volumen_litros = volumen_ml / 1000

            # Calculamos el precio por litro
            precio_litro = precio_venta / volumen_litros

            # Guardamos el resultado
            precios_venta_litro[nombre] = precio_litro

        # Devolvemos todos los precios por litro
        return precios_venta_litro
    def crear_precios_bebidas(catalogo_bebidas):

        # Creamos el objeto encargado de calcular los precios
        precios_bebidas = PreciosBebidas(catalogo_bebidas)

        # Devolvemos el objeto
        return precios_bebidas