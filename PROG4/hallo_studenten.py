"""
hallo_studenten.py

Dit is een scriptje, waarin we oefenen met functies en hallo zeggen tegen de studenten.

Usage:
    python hallo_studenten.py

@copyright  Hogeschool Utrecht, 2024
@author     Lina Blijleven
"""


def hallo(naam):
    """
    Zeg hallo tegen de student waarvan de naam is gegeven.

    :param naam:    str     Naam van de student als string
    :return:        None
    """
    print(f"Hallo {naam}")
    # We gebruiken geen return, er hoeft geen informatie teruggegeven te worden.

# Maak een lijstje met alle studenten
studenten = ["Ali", "Nick", "Hassan", "Tim", "Rohan", "Jenthyno"]

# Zeg hallo tegen allemaal!
for student in studenten:
    hallo(student)
