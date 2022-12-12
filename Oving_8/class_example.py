# Eksempel (?) fra forelesning
from unittest import result


class flervalgsporsmal:
    def __init__(self, tekst, alternativer, korrekt_alternativ):
        self.tekst = tekst
        self.alternativer = alternativer
        self.korrekt_alternativ = korrekt_alternativ

    def __str__(self):
        resultat = "Flervalgsspørsmål: " + self.tekst + "\n"
        for i, a in enumerate(self.alternativer):
            resultat += f"{i}: {a}\n"
        return resultat
    
    def sjekk_svar(self, bruker_svar):
        if bruker_svar == self.korrekt_alternativ:
            return True
        else:
            return False


if __name__ == "__main__":
    teksten = "Hva er hovedstadetn i Norge?"
    alternativ = ["Bergen", "Stavanger", "Oslo", "Stockholm"]
    korrekt_alternativ = 2
    sporsmal = flervalgsporsmal(teksten, alternativ, korrekt_alternativ)
    print(sporsmal)
    bruker_svar = int(input("Skriv inn svar: "))
    if sporsmal.sjekk_svar(bruker_svar):
        print("Yay")
    else:
        print("Feil")
