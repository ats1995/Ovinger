#dimsize = 9
dimsize = int(input("Skriv inn størrelse på diamant: "))
#print(dimsize*"_")
for i in range(dimsize):
    if i == 0:
        print((dimsize-1)*" ",end='')
        print("*")
    else:
        print((dimsize-i-1)*" ",end='')
        print("*",end='')
        print(((i)*2-1)*" ",end='')
        print("*")
for j in range(dimsize-1):
    if j == dimsize-2:
        print((j+1)*" ",end='')
        print("*")
    else:
        print((j+1)*" ",end='')
        print("*",end='')
        print(((dimsize-j)*2-5)*" ",end='')
        print("*")