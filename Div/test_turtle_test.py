import turtle
ssize = 50
angle_thus = 0
circle_angle = 15
turtle.setup(500,500,100,100)
turtle.speed(90)
#turtle.circle(ssize)
while angle_thus < 360:
    turtle.circle(ssize)
    turtle.right(circle_angle)
    angle_thus += circle_angle
turtle.done