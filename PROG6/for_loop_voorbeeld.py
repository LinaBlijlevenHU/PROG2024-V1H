pets = ['cat', 'dog', 'fish', 'bird']
namen = ["Garfield", "Wouter", "Blub", "Tweety"]

# Enhanced for-loop, element-wise for-loop
#for pet in pets:
#    print(pet, end="   ")

for i in range(len(pets)):
    pet = pets[i]
    name = namen[i]
    print(f"We have a {pet} at home named {name}.")
