# Task a:
# Skriv en klasse for land. Et land har et navn, en befolkning og et areal.
# Befolkning og areal skal ha default-verdier som sier at de ikke er satt enda.
# Navn skal ikke ha default-verdi.
class Country:
    def __init__(self, c_name: str, population = None, area = None):
        self.c_name = c_name
        self.population = population
        self.area = area
    
if __name__ == "__main__":
    norway = Country("Norway")
    print(norway.c_name)