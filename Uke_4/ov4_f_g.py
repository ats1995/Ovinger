from cmath import pi
def circ_area(r):
    return(pi*r*r)

def turbin_effekt(strom, tetthet=1000, turbin_effekt=0.3, diamater=1):
    energi = 0.5 * turbin_effekt * tetthet * circ_area(diamater/2) * strom**3
    return(energi)

tetth = 1000
turbe = 0.3
diam = 1

#tetth = float(input("Tetthet: "))
#turbe = float(input("Turbin effekt: "))
#diam = float(input("Daimeter: "))
if __name__ == "__main__":
    stro = float(input("Strøm: "))
    print(f"Energi: {turbin_effekt(stro, tetth, turbe, diam):.2f}")