def rng(lijst):
    """
    Vind het grootste getal in de lijst en haal daar het kleinste vanaf

    :param lijst:   Lijst met getallen (strings veroorzaakt errors)
    :return:        Het verschil tussen het grootste en kleinste getal
    """
    verschil = max(lijst) - min(lijst)
    return verschil


lijst = [-1, 5, -2, -59, 47]
print(rng(lijst))
