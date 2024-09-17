import math


def pythagoras(a, b):
    """
    Bereken de lengte van de schuine zijde met de stelling van Pythagoras
    :param a:   Lengte van de korte zijde (int/float)
    :param b:   Lengte van de lange zijde (int/float)
    :return:    Lengte van de schuine zijde (int/float)
    """
    return math.sqrt(a**2 + b**2)


print(pythagoras(3, 4))
