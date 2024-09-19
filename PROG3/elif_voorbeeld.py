# <61 onvoldoende
# >=61 punten voor voldoende
# >=76 punten voor boven niveau
# 95

punten_behaald = int(input("Hoeveel punten heb je behaald dit semester?"))

if punten_behaald >= 95:
    print("Heel goed gedaan! Je krijgt een extra mooie sticker.")
elif punten_behaald >= 76:
    print("Prestatie boven niveau")
elif punten_behaald >= 61:
    print("Voldoende voor semester behaald!")
else:
    print("Je hebt helaas het semester niet behaald.")
