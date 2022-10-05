start_bef = float(input("Start befolkning: "))
prosent_okning = float(input("Prosent økning: "))
år = float(input("Antall år: "))

befolkning = int(start_bef*(1+(prosent_okning/100))**år)
print("Befolkning etter", int(år), " år: ", befolkning)