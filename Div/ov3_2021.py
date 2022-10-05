import turtle
import time
turtle.setup(500,500,100,100)
turtle.speed(90)


diamanter = 139
walk = 10
didiff = 20

turtle.right(45)
for d in range(diamanter):
    for i in range(4):
        turtle.forward(walk)
        turtle.right(90)
    turtle.penup()
    turtle.back(didiff/2)
    turtle.left(90)
    turtle.forward(didiff/2)
    turtle.pendown()
    turtle.right(90)
    walk += didiff
time.sleep(1)