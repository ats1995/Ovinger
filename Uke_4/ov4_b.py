def posneg(inputnumber):
    if inputnumber >= 0:
        print(f"Verdien har steget med {inputnumber}")
    elif inputnumber < 0:
        print(f"Verdien har sunket med {abs(inputnumber)}")

posneg(int(input("Skriv inn et tall: ")))