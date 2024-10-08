SHIFT = 5

def shift_letter(char):
    """ Use ASCII to shift one letter a set amount of spots. """
    # Zet om naar ASCII ID + gewenste shift
    char_no = ord(char) + SHIFT
    # Zet terug om naar karakter
    return chr(char_no)

def shift_sentence(txt):
    """ Shift een hele zin """
    # Hier bouwen we de code op
    new_sentence = ""

    # Voor elk karakter in onze string
    for char in txt:
        new_char = shift_letter(char)
        new_sentence += new_char

    return new_sentence

print(shift_sentence('MarkRutteDen Helder'))