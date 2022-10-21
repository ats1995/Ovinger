# Task a:
# Skriv en klasse for land. Et land har et navn, en befolkning og et areal.
# Befolkning og areal skal ha default-verdier som sier at de ikke er satt enda.
# Navn skal ikke ha default-verdi.
# Task b:
# Skriv en __str__ metode for klassen Land. Denne metoden skal returnere en streng som
# inneholder navn, befolkning og areal til landet.
# Task c:
# Skriv en metode for klassen Land som regner ut og returnerer befolkningstettheten til landet.
# Befolkningstetthet er befolkning delt på areal.

class Country:
    def __init__(self, c_name: str, population = None, area = None):
        self.c_name = c_name
        self.population = population
        self.area = area
    
    def __str__(self):
        pop = ""
        ar = ""
        if self.population:
           pop = f", Population: {str(self.population)}"
        if self.area:
           ar = f", Area: {str(self.area)} km^2"
        return f"Name: {self.c_name}{pop}{ar}"
    
    def population_density(self):
        return self.population/self.area
    
if __name__ == "__main__":
    norway = Country("Norway", 7000000, 1500)
    print(norway)
#    print(f"{norway.population_density()}")
