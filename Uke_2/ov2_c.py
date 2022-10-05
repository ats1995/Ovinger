newTemp = float(input("New temperatur: "))
oldTemp = float(input("Old temperatur: "))
tempDiff = newTemp - oldTemp
if tempDiff < 0:
    print("Temperaturen har sunket med", abs(tempDiff), " grader.")
elif tempDiff > 0:
    print("Temperaturen har steget med", abs(tempDiff), " grader.")
elif tempDiff == 0:
    print("Temperaturen har ikke endret seg.")