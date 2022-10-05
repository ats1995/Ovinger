import math
a = float(input("a: "))
b = float(input("b: "))

area = math.pi * a * b
print(f"{area:6.2f}") # 'F-strenger, formatering
print("Arealet er: ", round(area, 2))
