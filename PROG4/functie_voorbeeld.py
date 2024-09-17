# Functie definitie
def kwadraatplus10(x):
    """
    Bereken x^2 + 10

    :param x:   Getal om te kwadrateren en 10 bij op te tellen
    :return:    Een kommagetal
    """
    res = x**2 + 10
    return res


# Functie aanroep
getal = 81
resultaat = kwadraatplus10(getal)
print(resultaat)

getallen = [0.6, 1, 2, 3, 4, 5]
for getal in getallen:
    print(kwadraatplus10(getal))