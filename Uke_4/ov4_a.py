import turtle
import time
#lines = int(input("Number lines: "))
lines = 9
walk = 5
turn = 90
turtle.setup(500,500,100,100)
turtle.speed(30)

for l in range(lines):
    for i in range(4):
        turtle.forward(walk)
        turtle.right(turn)
        walk += 5
time.sleep(1)