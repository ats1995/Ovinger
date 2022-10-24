# Skriv et script som lister ut gangetabell

storrelse = int(input("Tabellstørrelsen: "))

for tall in range(1, storrelse+1):
    print(f" {tall:3}", end="")
print()

for tall in range(storrelse):
    print("----", end="")
print()

for tall in range(1, storrelse+1):
    print(f" {tall:2}: ", end="")
    for tall2 in range(1, storrelse+1):
        resultat = tall*tall2
        print(f" {resultat:3}", end="")
    print()
