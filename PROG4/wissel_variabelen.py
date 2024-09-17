# Variabelen
a = 3
b = 6
print(f"Voor de eerste wissel {a}, {b}")

# 1. Variabelen omwisselen (taalonafhankelijk)
# Wisselen met een extra variabele
# Tijdelijke kopie van a
tmp = a
# Overschrijf a met b
a = b
# Overschrijf b met de kopie van a
b = tmp
print(f"Na de eerste wissel {a}, {b}")

# 2. Python-manier
a, b = b, a
print(f"Na de tweede wissel {a}, {b}")
