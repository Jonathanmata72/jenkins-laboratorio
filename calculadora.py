
def calcular_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("Precio invalido")

    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("Descuento invalido")

    descuento = precio * porcentaje / 100
    return precio - descuento
