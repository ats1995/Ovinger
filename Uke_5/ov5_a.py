malinger = int(input("Skriv inn antall målinger: "))
total = int(input("Skriv inn totalen: "))

def gjennomsnitt(ant, tot):
    return(float(tot/ant))

print(f"Gjennomsnittet er: {gjennomsnitt(malinger, total)}")