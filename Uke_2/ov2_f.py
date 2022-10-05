import math
import random
import sys
if len(sys.argv) > 1:
    sruntimes = int(sys.argv[1])
else:
    sruntimes = int(input("Skriv inn antall ganger vi skal kjøre testen: "))

insideCircle = int(0)
skudd = [[random.random(),random.random()]]
for i in range(sruntimes):
    skudd.append([random.random(),random.random()])
    if math.sqrt((skudd[i][0]**2) + (skudd[i][1]**2)) <= float(1):
        insideCircle += 1
print("Innenfor sirkel: ", insideCircle, "/", sruntimes)
estipi = float((insideCircle/sruntimes)*4)
print("Estimert pi: ", estipi)