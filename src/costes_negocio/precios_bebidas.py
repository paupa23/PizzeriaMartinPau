
from src.datos.bebidas import bebidas


def calcular_precios_venta_litro():
    # Diccionario para almacenar los precios de venta por litro
    precios_venta_litro = {}

    # Recorremos las bebidas del catálogo
    for nombre, datos in bebidas.items():
        precio_venta = datos["precio_venta"]

        # Extraemos los mililitros del formato
        volumen_ml = float(datos["formato"].replace(" ml", ""))

        # Convertimos mililitros a litros
        volumen_litros = volumen_ml / 1000

        # Calculamos el precio de venta por litro
        precios_venta_litro[nombre] = precio_venta / volumen_litros

    return precios_venta_litro


# Calculamos los precios de venta por litro
precios_venta_litro = calcular_precios_venta_litro()