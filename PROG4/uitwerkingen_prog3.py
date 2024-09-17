"""
uitwerkingen_prog3.py
"""

# Slide 17: spellingsprogramma
#Write a “spelling” program that:
#1) Requests a word from the user (woord is een string, dus geen conversie)
word = input("Wat is je favoriete woord?\n")

#2) Prints the characters in the word from left to right, one per line
print(f"Zo spel je dit!")
for char in word:
    print(char)
# Lege regel voor het overzicht
print()

# Slide 19
# a) 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#range(10)
#range(0, 10)
#range(0, 10, 1)

for i in range(10):
    print(i)
print()

# b) 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1, 10):
    print(i)
print()

# c) 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)
print()

# d) 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)
print()

# e) 20, 30, 40, 50, 60
for i in range(20, 70, 10):
    print(i)
print()
