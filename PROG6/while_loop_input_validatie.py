def vraag_naam():
    # Eindresultaat
    naam = ""
    studenten = ["Hassan", "Rohan", "Nick", "Charli", "Othman", "Tim", "Maurits"]

    while naam not in studenten:

        # We vragen om een naam (mogelijk nog niet eindresultaat)
        ans = input("Wat is je naam?").capitalize()

        # Is dit een geldige naam?
        if ans in studenten:
            # Overschrijf het eindresultaat met de naam van de gemachtigde student
            naam = ans

    return naam


naam = vraag_naam()
print(f"Je bent nu ingelogd, {naam}.")
