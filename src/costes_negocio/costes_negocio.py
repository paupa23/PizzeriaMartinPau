# Previsión mensual de ventas según la temporada
prevision_ventas = {
    "baja": {"pizzas": 1000, "bebidas": 600},
    "media": {"pizzas": 1500, "bebidas": 900},
    "alta": {"pizzas": 2200, "bebidas": 1400}
}

# Gastos fijos mensuales del negocio
gastos_mensuales = {
    "personal": 3000.00,
    "alquiler": 1200.00,
    "electricidad": 300.00,
    "agua": 60.00,
    "gas": 120.00,
    "seguros": 100.00,
    "gestoria": 80.00
}

# Precios medios estimados de venta sin IVA
precio_medio_pizza = 10.00
precio_medio_bebida = 1.60


def calcular_gastos_mensuales():
    # Sumamos todos los gastos mensuales
    return sum(gastos_mensuales.values())


def calcular_reparto_gastos(temporada):
    # Comprobamos que la temporada exista
    if temporada not in prevision_ventas:
        raise ValueError(f"Temporada no válida: {temporada}")

    # Obtenemos las unidades previstas de venta
    ventas = prevision_ventas[temporada]
    pizzas_mes = ventas["pizzas"]
    bebidas_mes = ventas["bebidas"]

    if pizzas_mes <= 0 or bebidas_mes <= 0:
        raise ValueError("Las ventas previstas deben ser positivas")

    # Calculamos los ingresos previstos de cada categoría
    ingresos_pizzas = pizzas_mes * precio_medio_pizza
    ingresos_bebidas = bebidas_mes * precio_medio_bebida
    ingresos_totales = ingresos_pizzas + ingresos_bebidas

    if ingresos_totales <= 0:
        raise ValueError("Los ingresos previstos deben ser positivos")

    # Repartimos los gastos según la proporción de ingresos
    gastos_totales = calcular_gastos_mensuales()
    proporcion_pizzas = ingresos_pizzas / ingresos_totales
    proporcion_bebidas = ingresos_bebidas / ingresos_totales

    gastos_pizzas = gastos_totales * proporcion_pizzas
    gastos_bebidas = gastos_totales * proporcion_bebidas

    # Calculamos los gastos asignados a cada unidad vendida
    return {
        "gastos_totales": round(gastos_totales, 2),
        "gastos_pizzas": round(gastos_pizzas, 2),
        "gastos_bebidas": round(gastos_bebidas, 2),
        "gasto_por_pizza": round(gastos_pizzas / pizzas_mes, 4),
        "gasto_por_bebida": round(gastos_bebidas / bebidas_mes, 4)
    }


def calcular_precio_venta(coste_total, margen_beneficio, iva):
    # Validamos los valores recibidos
    if coste_total < 0:
        raise ValueError("El coste no puede ser negativo")

    if not 0 <= margen_beneficio < 1:
        raise ValueError("El margen debe ser >= 0 y < 1")

    if iva < 0:
        raise ValueError("El IVA no puede ser negativo")

    # Calculamos el precio necesario para obtener el margen deseado
    precio_sin_iva = coste_total / (1 - margen_beneficio)

    # Calculamos el IVA y el precio final
    importe_iva = precio_sin_iva * iva
    precio_final = precio_sin_iva + importe_iva

    # Calculamos el beneficio antes de otros impuestos
    beneficio = precio_sin_iva - coste_total

    return {
        "coste_total": round(coste_total, 2),
        "precio_sin_iva": round(precio_sin_iva, 2),
        "iva": round(importe_iva, 2),
        "precio_final": round(precio_final, 2),
        "beneficio": round(beneficio, 2)
    }
