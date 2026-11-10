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
    def calcular_coste(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        # Si el ingrediente se compra por kg,
        # convertimos los gramos de la receta a kg
        if self.unidad == "kg":
            cantidad_convertida = cantidad / 1000
        # Si se compra por litros,
        # convertimos los mililitros de la receta a litros
        elif self.unidad == "l":
            cantidad_convertida = cantidad / 1000
        # Si se compra por unidades,
        # no necesitamos realizar ninguna conversión
        elif self.unidad == "unidad":
            cantidad_convertida = cantidad
        # Si utilizamos una unidad que no conocemos,
        # mostramos un error
        else:
            raise ValueError(f"Unidad no válida: {self.unidad}")
        # Multiplicamos el precio por la cantidad convertida
        return self.precio * cantidad_convertida