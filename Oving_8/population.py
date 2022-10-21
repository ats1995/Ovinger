from encodings import utf_8
from country_class import Country
#from highest_population import *

countries = dict()
with open("Oving_8/befolkning_tabell_csv.txt", encoding="UTF-8") as file:
    for line in file:
        line = line.split(";")
        countries[line[0]] = Country(line[0], line[1])

#print(f"{countries[])
for i in countries:
#    print(f"{i} - {countries[i]}")
    print(f"{countries[i].c_name} - {countries[i].population}")

print(countries["Malta"])

# Task f:
with open("Oving_8/areal_tabell_csv.txt", encoding="UTF-8") as file:
    for line in file:
        line = line.split(";")
        try:
            countries[line[0]].area = line[1]
            print(countries[line[0]])
        except KeyError:
            print(f"Could not find {line[0]}")

# Task g:
max_ppc = 0
max = "Malta"
for c in countries:
    if countries[c].population and countries[c].area:
        print(f"{countries[c]}")
        ppc = int(countries[c].population)/int(countries[c].area)
        print(f"Denisty: {ppc} persons/km^2")
        if ppc > max_ppc:
            max = countries[c].c_name
        #print(f"Denisty: {int(countries[c].population)/int(countries[c].area)} persons/km^2")
    elif not countries[c].area:
        print(f"{countries[c].c_name} does not have area defined")

print(f"Max density: {max}")
