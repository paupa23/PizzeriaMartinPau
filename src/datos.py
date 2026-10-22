pizzas = {
"Margarita": {
"masa": 220,
"tomate": 100,
"mozzarella": 200,
"albahaca": 4,
"aceite": 15,
"pimienta": 2,
"sal": 3
},

"Hawaiana": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 200,
    "jamon_cocido": 150,
    "piña": 100,
    "aceite": 15,
    "oregano": 50
},

"Cuatro_quesos": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 150,
    "queso_azul": 100,
    "parmesano": 100,
    "queso_suave": 100,
    "aceite": 15
},

"Cheetos": {
    "nata": 100,
    "mozzarella": 120,
    "cheddar": 50,
    "bacon": 70,
    "bolsa_cheetos": 0.5,
    "aceite": 15
},

"Caprichosa": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 120,
    "jamon_cocido": 100,
    "champiñones": 3,
    "alcachofa": 1,
    "olivas_negras": 8,
    "aceite": 15,
    "oregano": 50
},

"Cuatro_estaciones": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 120,
    "champiñones": 3,
    "alcachofa": 3,
    "olivas_negras": 10,
    "jamon_cocido": 100,
    "aceite": 15
},

"Barbacoa": {
    "masa": 220,
    "tomate": 100,
    "salsa_barbacoa": 40,
    "mozzarella": 120,
    "pechuga_pollo": 100,
    "carne_picada_vacuno": 100,
    "bacon": 50,
    "cebolla_morada": 0.5,
    "aceite": 15
},

"Carbonara": {
    "masa": 220,
    "nata": 100,
    "mozzarella": 120,
    "bacon": 100,
    "cebolla_blanca": 0.5,
    "champiñones": 3,
    "huevo": 2,
    "parmesano": 30,
    "pimienta": 2,
    "aceite": 15
},

"Burger": {
    "masa": 220,
    "salsa_barbacoa": 20,
    "mozzarella": 120,
    "cheddar": 60,
    "carne_picada_mixta": 100,
    "bacon": 50,
    "salsa_burger": 25,
    "aceite": 15
},

"Carnivora": {
    "masa": 220,
    "tomate": 100,
    "mezcla_quesos": 180,
    "carne_picada_vacuno": 90,
    "pechuga_pollo": 80,
    "jamon_cocido": 70,
    "pepperoni": 14,
    "aceite": 15
},

"Kebab": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "pollo_marinado": 40,
    "cebolla_blanca": 1,
    "especias_kebab": 20,
    "oregano": 50,
    "salsa_kebab": 30
},

"Bacon": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "bacon": 20,
    "salsa_barbacoa": 30
},

"Pepperoni": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "pepperoni": 40
},

"Prosciutto_funghi": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "jamon_cocido": 60,
    "champiñones": 40,
    "oregano": 50
},

"Napolitana": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "albahaca": 50,
    "alcaparras": 40,
    "olivas_negras": 40,
    "anchoas": 20
},

"Vegetal": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "cebolla_blanca": 1,
    "pimiento": 1,
    "champiñones": 50,
    "olivas_negras": 40
},

"Marinara": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "gambas": 20,
    "calamar": 20,
    "mejillones": 20,
    "oregano": 50,
    "perejil": 40
},

"Jamon_queso": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "jamon_cocido": 80,
    "aceite": 15
},

"Melanzane": {
    "masa": 220,
    "tomate": 100,
    "mozzarella": 100,
    "berenjena": 1,
    "pimiento": 1,
    "albahaca": 50,
    "rucula": 50,
    "vinagre": 1,
    "aceite": 15
},

"Pesto": {
    "masa": 220,
    "mozzarella": 100,
    "salsa_pesto": 100,
    "tomates_cherry": 20,
    "albahaca": 50,
    "aceite": 15
}
}

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
