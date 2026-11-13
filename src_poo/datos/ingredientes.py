class Ingrediente:
    def __init__(self, nombre, precio, unidad):
        # Guardamos el nombre del ingrediente
        self.nombre = nombre
        # Guardamos el precio de compra
        self.precio = precio
        # Guardamos la unidad en la que se compra
        # Puede ser kg, l o unidad
        self.unidad = unidad

    # Calcula el coste de una determinada cantidad del ingrediente
def calcular_coste(self, cantidad, unidad_receta="g", peso_unidad_g=None):

    # Comprobamos que la cantidad no sea negativa
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")

    # Comprobamos que la unidad de la receta sea válida
    if unidad_receta not in ("g", "ml", "l", "unidad"):
        raise ValueError(f"Unidad no válida: {unidad_receta}")

    # Si el ingrediente se compra por kg
    if self.unidad == "kg":

        # Si la receta está expresada en gramos
        if unidad_receta == "g":
            cantidad_convertida = cantidad / 1000

        # Si la receta está expresada en unidades
        elif unidad_receta == "unidad":

            # Necesitamos conocer el peso de una unidad
            if peso_unidad_g is None:
                raise ValueError(
                    f"No se conoce el peso por unidad de {self.nombre}"
                )

            # Convertimos las unidades a gramos
            gramos = cantidad * peso_unidad_g

            # Convertimos los gramos a kg
            cantidad_convertida = gramos / 1000

        else:
            raise ValueError(
                f"No se puede utilizar {unidad_receta} "
                f"para un ingrediente comprado por kg"
            )

    # Si el ingrediente se compra por litros
    elif self.unidad == "l":

        # Si la receta está expresada en mililitros
        if unidad_receta == "ml":
            cantidad_convertida = cantidad / 1000

        # Si la receta está expresada en litros
        elif unidad_receta == "l":
            cantidad_convertida = cantidad

        else:
            raise ValueError(
                f"No se puede utilizar {unidad_receta} "
                f"para un ingrediente comprado por litros"
            )

    # Si el ingrediente se compra por unidades
    elif self.unidad == "unidad":

        # La receta también debe estar expresada en unidades
        if unidad_receta != "unidad":
            raise ValueError(
                f"El ingrediente {self.nombre} debe utilizarse "
                f"en unidades"
            )

        cantidad_convertida = cantidad

    else:
        raise ValueError(f"Unidad de compra no válida: {self.unidad}")

    # Multiplicamos el precio por la cantidad convertida
    return self.precio * cantidad_convertida