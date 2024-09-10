# De input functie geeft ons altijd een string
ans = input("Wat is je leeftijd?\n")

# Als we hier het type printen krijgen we dus een string
print(type(ans))

# Cast de leeftijd naar een integer
leeftijd = int(ans)

# Impliciet casten naar string voor printen (leeftijd blijft een int)
# Als we werken met f-strings, hoeven we de variabelen die we gebruiken
# niet om te zetten naar strings van tevoren.
print(f"Volgend jaar wordt je {leeftijd+1}")

# Expliciet casten naar string voor printen (leeftijd moet eerst een string worden)
# Als we met de + (concatenation) operator werken, zullen we de berekening moeten doen met integers
# en hierna de nieuwe leeftijd weer om moeten zetten naar een string om te printen.
print("Volgend jaar wordt je " + str(leeftijd + 1))