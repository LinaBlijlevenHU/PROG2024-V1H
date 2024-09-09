"""
Lijst demo

Demo over werken met strings in lijsten.
Zie ook lijst_voorbeelden_getallen.py voor voorbeelden die toegepast worden op een lijst van getallen.
"""

# Maak een lijstje van studenten
studenten = ["Nick", "Jenthyno", "Maurits", "Bilal", "Tim", "Bob", "Hassan"]
studenten2 = ["Bram", "Mohamed"]

# Check of een naam voorkomt in de lijst
print("Noureddine" in studenten)

# Check of een naam niet voorkomt in de lijst
print("Julia" not in studenten)

# Lijsten samenvoegen
volledig = studenten + studenten2 + ["Noureddine"]
print(len(volledig))
print(volledig)

# Vervang een student door een andere student
volledig[5] = "Ali"

print(f"De lijst nadat een student is vervangen: {volledig}")

# Voeg iemand toe aan de lijst
volledig.append("Bob")
volledig.insert(0, "Roy")
print(f"De lijst nadat er studenten zijn toegevoegd: {volledig}")

# Voeg nog twee keer Tim toe aan de klas
volledig = volledig + ["Tim", "Tim"]
# Tel het aantal Tim's in de klas
print(volledig.count("Tim"))

print(f"De eerste Tim in de lijst staat op index {volledig.index("Tim")}")

# Pop: haal een element van de lijst en geef deze terug.
leerling = volledig.pop()
print(f"Tijd om een gesprek te plannen met {leerling}")

# Remove: verwijder een element op basis van naam (verwijdert automatisch het
# eerste voorkomen).
# We verwijderen één van de Tim's uit de lijst.
volledig.remove("Tim")
print(f"Er zitten nu {volledig.count("Tim")} Tim's in de klas.")

# Reverse
volledig.reverse()
print(f"Studentenlijst reversed: {volledig}")

# Sorteer op alfabet!
# Python begrijpt dat de a eerder voorkomt in het alfabet dan de z. Op basis hiervan
# kunnen we de min, max en sorteer-functies gebruiken die we ook met getallen gebruiken.
volledig.sort()

# Sorteer op alfabet (maar dan andersom)
#volledig.sort(reverse=True)

print(f"Studentenlijst gesorteerd op alfabet: {volledig}")