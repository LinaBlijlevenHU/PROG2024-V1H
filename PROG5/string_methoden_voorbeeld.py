link = "https://canvas.hu.nl/courses/44597/pages/prog5-text-data-strings-and-file-i-slash-o"

# Link split
print(link.split('/'))

# Paginanaam zoeken en ik weet dat hij met PROG5 begint.
page_name_start = link.find('prog5')
print(f"De naam van de pagina begint op index {page_name_start}")

# Selecteer vanaf het begin (index) van prog5 de naam van de pagina (t/m het einde)
page_name = link[page_name_start:]
print(page_name)