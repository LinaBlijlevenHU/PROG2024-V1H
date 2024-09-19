def is_klaar():
    """ Vraag de speler of deze klaar is """
    ans = input("Ben je klaar om te spelen? ja/nee: ")
    return ans.lower() in ["ja", "yes", "y", "j", "jup", "yessss"]


def speel_spelletje():
    """ Kijk of de gebruiker klaar is om te spelen """
    naam = input("Wat is je naam? ")

    # Vraag de speler of die klaar is om te spelen
    if is_klaar():
        print(f"{naam.capitalize()}, tijd om te spelen!")


# Functie aanroepen: begin het spel
speel_spelletje()
