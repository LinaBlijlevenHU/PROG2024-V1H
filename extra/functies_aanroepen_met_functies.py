def standaardprijs():
    return 50


def prijsmetkorting(percentage):
    standaard_prijs = standaardprijs()
    prijs = standaard_prijs - ((percentage/100) * standaard_prijs)
    return prijs

print(prijsmetkorting(10))
