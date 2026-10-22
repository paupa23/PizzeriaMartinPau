precios_ingredientes = {

    # 1. Masas y básicos
    "harina": {"precio": 0.72, "unidad": "kg"},
    "levadura": {"precio": 10.00, "unidad": "kg"},
    "agua": {"precio": 0.33, "unidad": "l"},
    "sal": {"precio": 0.40, "unidad": "kg"},
    "aceite": {"precio": 3.70, "unidad": "l"},

    # 2. Quesos y lácteos
    "mozzarella": {"precio": 8.00, "unidad": "kg"},
    "cheddar": {"precio": 9.75, "unidad": "kg"},
    "gouda": {"precio": 6.50, "unidad": "kg"},
    "queso_azul": {"precio": 12.78, "unidad": "kg"},
    "parmesano": {"precio": 16.50, "unidad": "kg"},
    "queso_suave": {"precio": 7.64, "unidad": "kg"},
    "emmental": {"precio": 6.37, "unidad": "kg"},
    "havarti": {"precio": 9.33, "unidad": "kg"},
    "nata": {"precio": 3.08, "unidad": "l"},

    # 3. Carnes
    "jamon_cocido": {"precio": 11.25, "unidad": "kg"},
    "bacon": {"precio": 9.20, "unidad": "kg"},
    "panceta_italiana": {"precio": 15.00, "unidad": "kg"},
    "pechuga_pollo": {"precio": 7.70, "unidad": "kg"},
    "pollo_marinado": {"precio": 8.20, "unidad": "kg"},
    "carne_picada_vacuno": {"precio": 11.00, "unidad": "kg"},
    "carne_picada_mixta": {"precio": 8.20, "unidad": "kg"},
    "pepperoni": {"precio": 21.33, "unidad": "kg"},

    # 4. Verduras, frutas y hierbas
    "cebolla_blanca": {"precio": 1.50, "unidad": "kg"},
    "cebolla_morada": {"precio": 1.40, "unidad": "kg"},
    "champiñones": {"precio": 5.56, "unidad": "kg"},
    "alcachofa": {"precio": 2.53, "unidad": "kg"},
    "pimiento_rojo": {"precio": 2.89, "unidad": "kg"},
    "pimiento_verde": {"precio": 2.80, "unidad": "kg"},
    "salsa_tomate": {"precio": 1.25, "unidad": "kg"},
    "tomates_cherry": {"precio": 4.40, "unidad": "kg"},
    "berenjena": {"precio": 2.20, "unidad": "kg"},
    "rucula": {"precio": 17.00, "unidad": "kg"},
    "ajo": {"precio": 7.40, "unidad": "kg"},
    "piña": {"precio": 2.00, "unidad": "kg"},
    "albahaca": {"precio": 77.50, "unidad": "kg"},
    "perejil": {"precio": 23.75, "unidad": "kg"},
    "oregano": {"precio": 40.00, "unidad": "kg"},

    # 5. Pescados y mariscos
    "gambas": {"precio": 13.61, "unidad": "kg"},
    "calamar": {"precio": 15.97, "unidad": "kg"},
    "mejillones": {"precio": 9.09, "unidad": "kg"},
    "anchoas": {"precio": 17.50, "unidad": "kg"},

    # 6. Salsas y condimentos
    "salsa_barbacoa": {"precio": 3.29, "unidad": "kg"},
    "salsa_burger": {"precio": 5.60, "unidad": "l"},
    "salsa_kebab": {"precio": 4.03, "unidad": "l"},
    "vinagre": {"precio": 4.60, "unidad": "l"},
    "pimienta": {"precio": 18.57, "unidad": "kg"},
    "especias_kebab": {"precio": 24.19, "unidad": "kg"},
    "olivas_negras": {"precio": 12.84, "unidad": "kg"},
    "alcaparras": {"precio": 10.00, "unidad": "kg"},
    "piñones": {"precio": 50.71, "unidad": "kg"},

    # 7. Otros ingredientes
    "huevo": {"precio": 0.24, "unidad": "unidad"},
    "bolsa_cheetos": {"precio": 1.89, "unidad": "bolsa"},
}


def calcular_coste_ingrediente(ingrediente, cantidad):
    # Obtenemos el precio y la unidad del ingrediente
    datos = precios_ingredientes[ingrediente]

    precio = datos["precio"]
    unidad = datos["unidad"]

    # Si el ingrediente se compra por kilogramo,
    # convertimos los gramos de la receta a kilogramos.
    if unidad == "kg":
        coste = (cantidad / 1000) * precio

    # Si se compra por litro, convertimos mililitros a litros.
    elif unidad == "l":
        coste = (cantidad / 1000) * precio

    # Si se compra por unidades, multiplicamos directamente.
    elif unidad == "unidad":
        coste = cantidad * precio

    else:
        raise ValueError(f"Unidad no reconocida: {unidad}")

    return coste
