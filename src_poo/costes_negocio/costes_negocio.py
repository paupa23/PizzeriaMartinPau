from src_poo.datos.ingredientes import Ingrediente
from src.costes_negocio.precios_ingredientes import (
    peso_unidad_g,
    precios_ingredientes,
)

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

    def agregar_ingrediente(self, nombre, precio, unidad):
        ingrediente = Ingrediente(nombre, precio, unidad)
        self.ingredientes[nombre] = ingrediente

    def obtener_ingrediente(self, nombre):
        if nombre not in self.ingredientes:
            raise ValueError(f"No existe el ingrediente: {nombre}")
        return self.ingredientes[nombre]

    def calcular_coste_masa(self):
        coste_harina = self.obtener_ingrediente("harina").calcular_coste(250, "g")
        coste_agua = self.obtener_ingrediente("agua").calcular_coste(160, "ml")
        coste_aceite = self.obtener_ingrediente("aceite").calcular_coste(25, "ml")
        coste_levadura = self.obtener_ingrediente("levadura").calcular_coste(10, "g")
        coste_sal = self.obtener_ingrediente("sal").calcular_coste(4, "g")

        coste_total = (
            coste_harina + coste_agua + coste_aceite + coste_levadura + coste_sal
        )
        return coste_total * (220 / 449)

    def calcular_coste_mezcla_quesos(self):
        coste_total = 0
        for nombre_queso in quesos_mezcla:
            coste_total += self.obtener_ingrediente(nombre_queso).precio
        return coste_total / len(quesos_mezcla)


def crear_catalogo_ingredientes():
    catalogo = CatalogoIngredientes()
    for nombre, datos in precios_ingredientes.items():
        catalogo.agregar_ingrediente(nombre, datos["precio"], datos["unidad"])
    return catalogo


class CostesNegocio:

    # Constructor de la clase
    def __init__(self):

        # Previsión de ventas mensuales
        self.prevision_ventas = {
            "baja": {"pizzas": 1000, "bebidas": 600},
            "media": {"pizzas": 1500, "bebidas": 900},
            "alta": {"pizzas": 2200, "bebidas": 1400},
        }

        # Gastos mensuales del negocio
        self.gastos_mensuales = {
            "personal": 3000.00,
            "alquiler": 1200.00,
            "electricidad": 300.00,
            "agua": 60.00,
            "gas": 120.00,
            "seguros": 100.00,
            "gestoria": 80.00,
        }

        self.precio_medio_pizza = 10.00
        self.precio_medio_bebida = 1.60

    def calcular_gastos_mensuales(self):
        return sum(self.gastos_mensuales.values())

    def calcular_reparto_gastos(self, temporada):
        if temporada not in self.prevision_ventas:
            raise ValueError(f"Temporada no válida: {temporada}")

        ventas = self.prevision_ventas[temporada]
        pizzas_mes = ventas["pizzas"]
        bebidas_mes = ventas["bebidas"]

        if pizzas_mes <= 0 or bebidas_mes <= 0:
            raise ValueError("Las ventas previstas deben ser positivas")

        ingresos_pizzas = pizzas_mes * self.precio_medio_pizza
        ingresos_bebidas = bebidas_mes * self.precio_medio_bebida
        ingresos_totales = ingresos_pizzas + ingresos_bebidas

        if ingresos_totales <= 0:
            raise ValueError("Los ingresos previstos deben ser positivos")

        gastos_totales = self.calcular_gastos_mensuales()
        proporcion_pizzas = ingresos_pizzas / ingresos_totales
        proporcion_bebidas = ingresos_bebidas / ingresos_totales

        gastos_pizzas = gastos_totales * proporcion_pizzas
        gastos_bebidas = gastos_totales * proporcion_bebidas

        return {
            "gastos_totales": round(gastos_totales, 2),
            "gastos_pizzas": round(gastos_pizzas, 2),
            "gastos_bebidas": round(gastos_bebidas, 2),
            "gasto_por_pizza": round(gastos_pizzas / pizzas_mes, 4),
            "gasto_por_bebida": round(gastos_bebidas / bebidas_mes, 4),
        }

    def calcular_precio_venta(self, coste_total, margen_beneficio, iva):
        if coste_total < 0:
            raise ValueError("El coste no puede ser negativo")

        if not 0 <= margen_beneficio < 1:
            raise ValueError("El margen debe ser >= 0 y < 1")

        if iva < 0:
            raise ValueError("El IVA no puede ser negativo")

        precio_sin_iva = coste_total / (1 - margen_beneficio)
        importe_iva = precio_sin_iva * iva
        precio_final = precio_sin_iva + importe_iva
        beneficio = precio_sin_iva - coste_total

        return {
            "coste_total": round(coste_total, 2),
            "precio_sin_iva": round(precio_sin_iva, 2),
            "iva": round(importe_iva, 2),
            "precio_final": round(precio_final, 2),
            "beneficio": round(beneficio, 2),
        }


# Crea y devuelve un objeto CostesNegocio
def crear_costes_negocio():
    return CostesNegocio()