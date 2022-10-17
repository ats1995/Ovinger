with open("Div/oving_1_rein_tekst.txt", encoding="UTF-8") as fila:
    linjenr = 1
    ord_oversikt = dict()
    for linje in fila:
        linje = linje.strip()
        ordene = linje.split(" ")
        for ordet in ordene:
            if ordet not in ord_oversikt:
                ord_oversikt[ordet] = linjenr
        linjenr += 1
    for ordet in ord_oversikt:
        print(f"Ordet \"{ordet}\" er første gang på linje {ord_oversikt[ordet]}")