def posneg(inputnumber):
    if inputnumber >= 0:
        print(f"Verdien har steget med {inputnumber}")
    elif inputnumber < 0:
        print(f"Verdien har sunket med {abs(inputnumber)}")

startVerdi = float(input("Startverdi: "))

while True:
    brukertall = float(input("Skriv inn ny temperatur: "))
    posneg(brukertall-startVerdi)
    startVerdi = brukertall