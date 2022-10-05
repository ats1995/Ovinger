from time import sleep
import turtle
kanter = int(input("Skriv inn antall kanter: "))
if kanter < 3:
    print("Dette blir ingen geometrisk form av.")
    exit()
#kanter = 5
turtle.setup(500,500,100,100)
for i in range(kanter):
    turtle.forward(600/kanter)
    turtle.right(360/kanter)
#sleep(1)
turtle.exitonclick()