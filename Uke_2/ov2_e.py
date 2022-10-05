startVerdi = float(input("Startverdi: "))

while startVerdi > 0:
    andreVerdi = float(input("Ny verdi: "))
    print("Differanse:", startVerdi - andreVerdi)
    startVerdi = andreVerdi
print("Du la inn et negativt tall, program avsluttes.")