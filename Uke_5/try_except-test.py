ni = 123
fl = 2.3
le = "asdf"
nt = str(ni)

print(type(nt))
try:
    float(ni)
    print("virket")
except ValueError:
    print("Neisann")