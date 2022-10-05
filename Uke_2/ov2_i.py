import turtle
import time
angle_thus = 0
circle_angle = 45
turtle.setup(500,500,100,100)
turtle.speed(90)
turtle.setheading(350)
while angle_thus < 360:
    turtle.setheading(angle_thus)
    ssize = 20
    circrot = 0
    for i in range(5):
        turtle.right(circrot)
        turtle.circle(ssize)
        ssize += 15
        circrot += 3
    turtle.right(circle_angle)
    angle_thus += circle_angle
turtle.done
time.sleep(1)