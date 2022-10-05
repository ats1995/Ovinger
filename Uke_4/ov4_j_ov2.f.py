import math
import random
import sys
insideCircle = int(0)
def distance(shot):
    return(math.sqrt((shot[0]**2) + (shot[1]**2)))
def inside_circle(shot):
    if distance(shot) <= float(1):
        global insideCircle
        insideCircle += 1

if len(sys.argv) > 1:
    sruntimes = int(sys.argv[1])
else:
    sruntimes = int(input("Skriv inn antall ganger vi skal kjøre testen: "))

for i in range(sruntimes):
    skudd = [random.random(),random.random()]
    inside_circle(skudd)
#print("Innenfor sirkel: ", insideCircle, "/", sruntimes)
estipi = float((insideCircle/sruntimes)*4)
print("Estimert pi: ", estipi)