"""Conecta el calculo de costes original con los precios del menu."""

from src.costes_negocio.costes_negocio import (
    calcular_precio_venta,
    calcular_reparto_gastos,
)
from src.costes_negocio.precios_pizzas import calcular_coste_pizza


# Coste unitario requerido por el enunciado.
SUMINISTROS_POR_PIZZA = 0.60
# Respetamos el margen del 35 % sobre venta definido por el companero.
MARGEN_BENEFICIO = 0.35
IVA = 0.10


def calcular_precio_pizza(nombre_pizza, temporada="media"):
    """Calcula el precio final usando las funciones originales del companero."""
    coste_ingredientes = calcular_coste_pizza(nombre_pizza)
    gastos_por_pizza = calcular_reparto_gastos(temporada)["gasto_por_pizza"]
    coste_total = coste_ingredientes + gastos_por_pizza + SUMINISTROS_POR_PIZZA

    resultado = calcular_precio_venta(coste_total, MARGEN_BENEFICIO, IVA)
    resultado["coste_ingredientes"] = round(coste_ingredientes, 2)
    resultado["gasto_fijo_por_pizza"] = gastos_por_pizza
    resultado["suministros_por_pizza"] = SUMINISTROS_POR_PIZZA
    resultado["temporada"] = temporada
    return resultado