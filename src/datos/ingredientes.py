from pizzas import pizzas

# Función para obtener la lista de ingredientes de todas las pizzas con pizzas.values()
def obtener_ingredientes(pizzas):
    # El conjunto {...} elimina duplicados
    return sorted({
    ingrediente
    for ingredientes_pizza in pizzas.values()
    for ingrediente in ingredientes_pizza
    })

# Catálogo general de ingredientes, generado automáticamente
ingredientes = obtener_ingredientes(pizzas)

print(ingredientes)


# Diccionario que indica la unidad de medida de los ingredientes
# cuando no podemos deducirla directamente de la receta.
#
# Permite distinguir, por ejemplo, entre 3 champiñones y 40 gramos
# de champiñones, aunque ambos utilicen la misma clave: "champiñones".
#
# Las unidades utilizadas serán:
# "g"      = gramos
# "ml"     = mililitros
# "unidad" = unidades individuales

unidades_ingredientes = {
    "Caprichosa": {
        "champiñones": "unidad",
        "alcachofa": "g",
        "olivas_negras": "unidad"
    },

    "Cuatro_estaciones": {
        "champiñones": "unidad",
        "alcachofa": "unidad",
        "olivas_negras": "unidad"
    },

    "Carbonara": {
        "champiñones": "unidad",
        "cebolla_blanca": "unidad",
        "huevo": "unidad"
    },

    "Barbacoa": {
        "cebolla_morada": "unidad"
    },

    "Kebab": {
        "cebolla_blanca": "unidad"
    },

    "Prosciutto_funghi": {
        "champiñones": "g"
    },

    "Napolitana": {
        "olivas_negras": "g"
    },

    "Vegetal": {
        "cebolla_blanca": "unidad",
        "pimiento_rojo": "g",
        "champiñones": "g",
        "olivas_negras": "g"
    },

    "Melanzane": {
        "berenjena": "unidad",
        "pimiento_verde": "g",
        "vinagre": "ml"
    },

    "Cheetos": {
        "bolsa_cheetos": "unidad"
    }
}