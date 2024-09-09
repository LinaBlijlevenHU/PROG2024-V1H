import random

#random.seed(86567890)

# Rol een dobbelsteen
dobbel = random.randrange(1, 7)
dobbel2 = random.randrange(1, 7)
print(f"Je hebt {dobbel} gerold!")
print(f"Je hebt {dobbel2} gerold!")

# Lijst met studenten
studenten = ["Nick", "Jenthyno", "Maurits", "Bilal", "Tim", "Bob", "Hassan"]

# Random shuffle van de studenten
random.shuffle(studenten)
print(studenten)

# Random sample van de studenten
leerteam = random.sample(studenten, 4)
print(leerteam)

# Kies een willekeurige klassenvoorzitter
voorzitter = random.choice(studenten)
print(f"De voorzitter van de klas wordt {voorzitter}")