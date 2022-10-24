total_passeringer = 0
maalestasjon = input("Skriv inn navnet på målestasjonen: ")
maaned = int(input("Skriv inn hvlken måned som et tall fra 1 til 12: "))
try:
    with open("sykkelpasseringer.txt", encoding="UTF8") as fila:
        for linje in fila:
            try:
                komponenter = linje.split(";")
                if komponenter[1] == maalestasjon:
                    dato = komponenter[2]
                    dato_komponenter = dato.split("-")
                    if int(dato_komponenter[1]) == maaned:
                        passeringer_str = komponenter[3]
                        passeringer = int(passeringer_str)
                        total_passeringer = passeringer
            except ValueError:
                pass
            # Kan ha flere 'except's !!
            except IndexError:
                pass
        print(f"Totalt antall passeringer for {maalestasjon} i måned {maaned}: {total_passeringer}")
except IOError as e:
    print("Klarer ikke å åpne filea!" + str(3))
