lijst = [1, 3, 5, 6, 8, 9, 0, 10]

som = 0

for getal in lijst:
    print(f"Het volgende getal om op te tellen is {getal}")
    print(f"De som is nu {som}")
    # OF som += getal (kortere notatie)
    som = som + getal

print(som)