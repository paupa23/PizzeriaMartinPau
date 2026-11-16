class CostesNegocio:

    # Constructor de la clase
    def __init__(self):

        # Previsión de ventas mensuales
        self.prevision_ventas = {
            "baja": {
                "pizzas": 1000,
                "bebidas": 600
            },
            "media": {
                "pizzas": 1500,
                "bebidas": 900
            },
            "alta": {
                "pizzas": 2200,
                "bebidas": 1400
            }
        }

        # Gastos mensuales del negocio
        self.gastos_mensuales = {
            "personal": 3000.00,
            "alquiler": 1200.00,
            "electricidad": 300.00,
            "agua": 60.00,
            "gas": 120.00,
            "seguros": 100.00,
            "gestoria": 80.00
        }

        # Precio medio de venta de una pizza
        self.precio_medio_pizza = 10.00

        # Precio medio de venta de una bebida
        self.precio_medio_bebida = 1.60

    # Calcula los gastos mensuales totales
    def calcular_gastos_mensuales(self):

        # Sumamos todos los gastos
        return sum(self.gastos_mensuales.values())

    # Calcula cómo se reparten los gastos entre pizzas y bebidas
    def calcular_reparto_gastos(self, temporada):

        # Comprobamos que la temporada exista
        if temporada not in self.prevision_ventas:
            raise ValueError(
                f"Temporada no válida: {temporada}"
            )

        # Obtenemos las ventas previstas
        ventas = self.prevision_ventas[temporada]

        # Obtenemos las unidades previstas
        pizzas_mes = ventas["pizzas"]
        bebidas_mes = ventas["bebidas"]

        # Comprobamos que las ventas sean positivas
        if pizzas_mes <= 0 or bebidas_mes <= 0:
            raise ValueError(
                "Las ventas previstas deben ser positivas"
            )

        # Calculamos los ingresos de las pizzas
        ingresos_pizzas = (
            pizzas_mes * self.precio_medio_pizza
        )

        # Calculamos los ingresos de las bebidas
        ingresos_bebidas = (
            bebidas_mes * self.precio_medio_bebida
        )

        # Calculamos los ingresos totales
        ingresos_totales = (
            ingresos_pizzas + ingresos_bebidas
        )

        # Comprobamos que los ingresos sean positivos
        if ingresos_totales <= 0:
            raise ValueError(
                "Los ingresos previstos deben ser positivos"
            )

        # Calculamos los gastos totales
        gastos_totales = self.calcular_gastos_mensuales()

        # Calculamos la proporción correspondiente a pizzas
        proporcion_pizzas = (
            ingresos_pizzas / ingresos_totales
        )

        # Calculamos la proporción correspondiente a bebidas
        proporcion_bebidas = (
            ingresos_bebidas / ingresos_totales
        )

        # Repartimos los gastos
        gastos_pizzas = (
            gastos_totales * proporcion_pizzas
        )

        gastos_bebidas = (
            gastos_totales * proporcion_bebidas
        )

        # Devolvemos los resultados
        return {
            "gastos_totales": round(gastos_totales, 2),
            "gastos_pizzas": round(gastos_pizzas, 2),
            "gastos_bebidas": round(gastos_bebidas, 2),
            "gasto_por_pizza": round(
                gastos_pizzas / pizzas_mes,
                4
            ),
            "gasto_por_bebida": round(
                gastos_bebidas / bebidas_mes,
                4
            )
        }

        # Calcula el precio de venta a partir del coste,
    # el margen de beneficio y el IVA
    def calcular_precio_venta(self, coste_total, margen_beneficio, iva):

        # Comprobamos que el coste no sea negativo
        if coste_total < 0:
            raise ValueError(
                "El coste no puede ser negativo"
            )

        # Comprobamos que el margen esté entre 0 y 1
        if not 0 <= margen_beneficio < 1:
            raise ValueError(
                "El margen debe ser >= 0 y < 1"
            )

        # Comprobamos que el IVA no sea negativo
        if iva < 0:
            raise ValueError(
                "El IVA no puede ser negativo"
            )

        # Calculamos el precio antes de aplicar el IVA
        precio_sin_iva = (
            coste_total / (1 - margen_beneficio)
        )

        # Calculamos el importe del IVA
        importe_iva = precio_sin_iva * iva

        # Calculamos el precio final
        precio_final = precio_sin_iva + importe_iva

        # Calculamos el beneficio
        beneficio = precio_sin_iva - coste_total

        # Devolvemos todos los resultados
        return {
            "coste_total": round(coste_total, 2),
            "precio_sin_iva": round(precio_sin_iva, 2),
            "iva": round(importe_iva, 2),
            "precio_final": round(precio_final, 2),
            "beneficio": round(beneficio, 2)
        }

# Crea y devuelve un objeto CostesNegocio
def crear_costes_negocio():
    costes_negocio = CostesNegocio()
    return costes_negocio