class Rom:
    def __init__(self, romtype, kapasitet, romnummer):
        self.romtype = romtype
        self.kapasitet = kapasitet
        self.romnummer = romnummer

def min_kapasitet(romliste, kapasitet):
    resultat = list()
    for rommet in romliste:
        if rommet.kapasitet >= kapasitet:
            resultat.append(rommet)
    return resultat