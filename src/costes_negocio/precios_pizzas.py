
from src.datos.pizzas import pizzas
from src.datos.ingredientes import unidades_ingredientes
from src.costes_negocio.precios_ingredientes import calcular_coste_ingrediente
from src.costes_negocio.precios_ingredientes import calcular_coste_masa


# Unidades predeterminadas para ingredientes líquidos
unidades_predeterminadas = {
    "aceite": "ml",
    "salsa_burger": "ml",
    "salsa_kebab": "ml",
    "vinagre": "ml"
}


def calcular_coste_pizza(nombre_pizza):
    # Comprobamos que la pizza exista
    if nombre_pizza not in pizzas:
        raise ValueError(f"No existe la pizza: {nombre_pizza}")

    # Obtenemos los ingredientes y cantidades de la pizza
    ingredientes_pizza = pizzas[nombre_pizza]

    # Obtenemos las unidades específicas de la receta
    unidades_pizza = unidades_ingredientes.get(nombre_pizza, {})

    # Inicializamos el coste total de la pizza
    coste_total = 0

    # Recorremos los ingredientes y cantidades de la pizza
    for ingrediente, cantidad in ingredientes_pizza.items():

        # Calculamos el coste de la masa proporcionalmente
        if ingrediente == "masa":
            coste = calcular_coste_masa() * (cantidad / 220)

        else:
            # Obtenemos la unidad correspondiente al ingrediente
            unidad_receta = unidades_pizza.get(
                ingrediente,
                unidades_predeterminadas.get(ingrediente, "g")
            )

            # Calculamos el coste del ingrediente
            coste = calcular_coste_ingrediente(
                ingrediente,
                cantidad,
                unidad_receta
            )

        # Sumamos el coste del ingrediente al total
        coste_total += coste

    return coste_total