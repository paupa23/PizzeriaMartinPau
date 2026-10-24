
precios_ingredientes = {
    # Ingredientes para la masa
    "harina": {"precio": 0.72, "unidad": "kg"},
    "agua": {"precio": 0.33, "unidad": "l"},
    "aceite": {"precio": 3.70, "unidad": "l"},
    "levadura": {"precio": 10.00, "unidad": "kg"},
    "sal": {"precio": 0.40, "unidad": "kg"},

    # Quesos
    "mozzarella": {"precio": 8.00, "unidad": "kg"},
    "cheddar": {"precio": 9.75, "unidad": "kg"},
    "gouda": {"precio": 6.50, "unidad": "kg"},
    "queso_azul": {"precio": 12.78, "unidad": "kg"},
    "parmesano": {"precio": 16.50, "unidad": "kg"},
    "queso_suave": {"precio": 7.64, "unidad": "kg"},
    "emmental": {"precio": 6.37, "unidad": "kg"},
    "havarti": {"precio": 9.33, "unidad": "kg"},

    # Lácteos
    "nata": {"precio": 3.08, "unidad": "l"},

    # Carnes
    "jamon_cocido": {"precio": 11.25, "unidad": "kg"},
    "bacon": {"precio": 9.20, "unidad": "kg"},
    "panceta_italiana": {"precio": 15.00, "unidad": "kg"},
    "pechuga_pollo": {"precio": 7.70, "unidad": "kg"},
    "pollo_marinado": {"precio": 8.20, "unidad": "kg"},
    "carne_picada_vacuno": {"precio": 11.00, "unidad": "kg"},
    "carne_picada_mixta": {"precio": 8.20, "unidad": "kg"},
    "pepperoni": {"precio": 21.33, "unidad": "kg"},

    # Verduras y hortalizas
    "cebolla_blanca": {"precio": 1.50, "unidad": "kg"},
    "cebolla_morada": {"precio": 1.40, "unidad": "kg"},
    "champiñones": {"precio": 5.56, "unidad": "kg"},
    "alcachofa": {"precio": 2.53, "unidad": "kg"},
    "pimiento_rojo": {"precio": 2.89, "unidad": "kg"},
    "pimiento_verde": {"precio": 2.80, "unidad": "kg"},
    "tomates_cherry": {"precio": 4.40, "unidad": "kg"},
    "berenjena": {"precio": 2.20, "unidad": "kg"},
    "rucula": {"precio": 17.00, "unidad": "kg"},
    "ajo": {"precio": 7.40, "unidad": "kg"},
    "piña": {"precio": 2.00, "unidad": "kg"},
    "albahaca": {"precio": 77.50, "unidad": "kg"},
    "perejil": {"precio": 23.75, "unidad": "kg"},
    "oregano": {"precio": 40.00, "unidad": "kg"},

    # Pescados y mariscos
    "gambas": {"precio": 13.61, "unidad": "kg"},
    "calamar": {"precio": 15.97, "unidad": "kg"},
    "mejillones": {"precio": 9.09, "unidad": "kg"},
    "anchoas": {"precio": 17.50, "unidad": "kg"},

    # Salsas y condimentos
    "salsa_tomate": {"precio": 1.25, "unidad": "kg"},
    "salsa_barbacoa": {"precio": 3.29, "unidad": "kg"},
    "salsa_burger": {"precio": 5.60, "unidad": "l"},
    "salsa_kebab": {"precio": 4.03, "unidad": "l"},
    "salsa_pesto": {"precio": 12.67, "unidad": "kg"},
    "vinagre": {"precio": 4.60, "unidad": "l"},
    "pimienta": {"precio": 18.57, "unidad": "kg"},
    "especias_kebab": {"precio": 24.19, "unidad": "kg"},
    "olivas_negras": {"precio": 12.84, "unidad": "kg"},
    "alcaparras": {"precio": 10.00, "unidad": "kg"},
    "piñones": {"precio": 50.71, "unidad": "kg"},

    # Otros ingredientes
    "huevo": {"precio": 0.24, "unidad": "unidad"},
    "bolsa_cheetos": {"precio": 1.89, "unidad": "unidad"},
}


# Peso aproximado por unidad en gramos
peso_unidad_g = {
    "champiñones": 10,
    "alcachofa": 170,
    "olivas_negras": 4,
    "cebolla_blanca": 150,
    "cebolla_morada": 150,
    "berenjena": 400,
}


# Todos los quesos participan en la mezcla en la misma proporción
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


def calcular_coste_mezcla_quesos():
    # Calcula el coste por kilogramo de la mezcla
    coste_total = 0

    for queso in quesos_mezcla:
        coste_total += precios_ingredientes[queso]["precio"]

    return coste_total / len(quesos_mezcla)


def calcular_coste_ingrediente(ingrediente, cantidad, unidad_receta="g"):
    # Comprueba que la cantidad sea válida
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    if unidad_receta not in ("g", "ml", "l", "unidad"):
        raise ValueError(f"Unidad de receta no válida: {unidad_receta}")

    # Calcula el precio de la mezcla de quesos dinámicamente
    if ingrediente == "mezcla_quesos":
        precio = calcular_coste_mezcla_quesos()
        unidad_compra = "kg"
    else:
        if ingrediente not in precios_ingredientes:
            raise ValueError(
                f"No existe el ingrediente: {ingrediente}"
            )

        datos = precios_ingredientes[ingrediente]
        precio = datos["precio"]
        unidad_compra = datos["unidad"]

        # Impide calcular ingredientes sin precio definido
        if precio is None:
            raise ValueError(
                f"Falta definir el precio de {ingrediente}."
            )

    # Convierte gramos a kilogramos
    if unidad_compra == "kg":
        if unidad_receta == "g":
            cantidad_convertida = cantidad / 1000

        elif unidad_receta == "unidad":
            if ingrediente not in peso_unidad_g:
                raise ValueError(
                    f"No se conoce el peso por unidad de {ingrediente}."
                )

            cantidad_convertida = (
                cantidad * peso_unidad_g[ingrediente] / 1000
            )

        else:
            raise ValueError(
                f"No se puede convertir {unidad_receta} a kg "
                f"para {ingrediente}."
            )

    # Convierte mililitros a litros
    elif unidad_compra == "l":
        if unidad_receta == "ml":
            cantidad_convertida = cantidad / 1000

        elif unidad_receta == "l":
            cantidad_convertida = cantidad

        else:
            raise ValueError(
                f"No se puede convertir {unidad_receta} a litros "
                f"para {ingrediente}."
            )

    # Calcula ingredientes comprados por unidad
    elif unidad_compra == "unidad":
        if unidad_receta != "unidad":
            raise ValueError(
                f"{ingrediente} se calcula por unidades."
            )

        cantidad_convertida = cantidad

    else:
        raise ValueError(
            f"Unidad de compra no reconocida: {unidad_compra}"
        )

    return precio * cantidad_convertida


def calcular_coste_masa():
    # Ingredientes y cantidades de la receta de masa
    ingredientes_masa = {
        "harina": (250, "g"),
        "agua": (160, "ml"),
        "aceite": (25, "ml"),
        "levadura": (10, "g"),
        "sal": (4, "g"),
    }

    coste_total = 0

    for ingrediente, (cantidad, unidad) in ingredientes_masa.items():
        coste_total += calcular_coste_ingrediente(
            ingrediente,
            cantidad,
            unidad
        )

    # Rendimiento aproximado en gramos de la receta completa
    rendimiento_masa_g = 449

    # Cantidad de masa utilizada por pizza
    peso_masa_pizza_g = 220

    return coste_total * peso_masa_pizza_g / rendimiento_masa_g
