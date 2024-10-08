PATH = "sample.txt"

import os

def read_content(fname):
    try:
        file = open(fname)
    except FileNotFoundError:
        print("File niet gevonden.")
        file = open(fname, 'w')
        file.close()
        file = open(fname, 'r')

    content = file.readlines()
    file.close()
    return content

def read_content2(fname):
    if not os.path.exists(fname):
        print("Pad bestaat nog niet :(")

read_content(PATH)