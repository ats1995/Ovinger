# Task d:
# Skriv en funksjon som tar inn to land, sjekker hvilket som har høyest befolkning, og
# returnerer landet som har høyest befolkning av de to.
from country_class import Country

def highest_population(country1: Country, country2: Country):
#   return max(country1.population, country2.population) 
    if country1.population > country2.population:
        return country1.c_name
    else:
        return country2.c_name

if __name__ == "__main__":
    norway = Country("Norway", 12342134)
    sweden = Country("Sweden", 23431453151, 4125)
    print(f"{highest_population(norway, sweden)}")