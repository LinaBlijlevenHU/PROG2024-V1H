import random

names = [
    "Azzy", "Bram", "Maurits", "Jorwin", "Othman", "Mohamed B",
    "Bilal", "Noureddine", "Mohamed H", "Hassan", "Nick H",
    "Rahim", "Jenthyno", "Roy", "Nick N", "Charli", "Rohan",
    "Tim IDR", "Twan", "Rens", "Ali", "Layco", "Thijs", "Tim V", "Tim W", "Bob"
]

x = len(names) // 3

random.shuffle(names)

print(f"Hagen krijgt {names[:x]}")
print(f"Lina krijgt {names[x:2*x]}")
print(f"Matthias krijgt {names[2*x:]}")


