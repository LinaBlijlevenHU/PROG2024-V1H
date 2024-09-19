"""
os_voorbeeld.py
"""

import os

output_path = "/output/"
fname = os.getcwd() + output_path + "studenten.txt"


# Waar we nu werken
#print(os.getcwd())
# Folder waar we heen schrijven (huidige folder + relatief pad)
#print(os.getcwd() + output_path)
# File waar we naartoe gaan schrijven (huidige folder + relatieve pad + filename)
#print(fname)

# Manier 1: file openen
open_file = open(fname)
# <Bewerkingen/lezen van de file hiertussen>
# bijv. all_lines = open_file.readlines()
open_file.close()

# Manier 2: file openen binnen context
with open(fname) as my_file:
    # read(): lees de hele file uit als één lange string
    content = my_file.read()
    print(type(content))            # 1 str

# r+ staat for read + write
with open(fname, 'r+') as my_file:
    # readlines(): lees de hele file uit, splits op \n en sla het resultaat op
    # als een lijst
    lines = my_file.readlines()
    print(type(lines))              # lijst?
    print(lines)

    # write(): schrijf een string naar een bestand
    my_file.write("De file is weer afgesloten.")



# File sluit nu vanzelf.


