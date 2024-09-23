"""
nested_for_loop.py
"""

table = [[3, 5, 7, 9], [0, 2, 1, 6], [3, 8, 3, 1]]

# Selecteer de eerste rij (is eerste element)
first_row = table[0]
seven = first_row[2]  # OF table[0][2]


def som2D(t):
    """ Tel alle getallen uit een 2-dimensionale lijst bij elkaar op """
    optelsom = 0

    # Voor elke rij
    for row in t:
        # Voor elk item in één rij
        for item in row:
            optelsom += item

    return optelsom


def print2D(t):
    """prints values in 2D list t as a 2D table"""
    # Voor elke rij in onze tabel
    for row in t:
        # Bekijk elk item in de rij
        for item in row:
            # Print het item
            print(item, end=' ')
        # Print een nieuwe regel voor de volgende rij
        print()


print2D(table)
print(f"De som van de hele 2D lijst is: {som2D(table)}")
