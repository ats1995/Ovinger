import turtle
import time
turtle.setup(500,500,100,100)
turtle.speed(1000)

def star(star_size):
    #star_size = 10
    for i in range(12):
        turtle.forward(star_size)
        turtle.back(star_size)
        turtle.right(30)

def galaxy(arms,galaxy_size):
    x = 0
    y = 0
    star_size = 10
    star(star_size)
    turtle.penup()
    star_distance = 30
    for j in range(galaxy_size):
        for i in range(arms):
            turtle.setheading(i*(360/arms)+(j**0.5*30))
            turtle.forward(star_distance*(j+1))
            turtle.pendown()
            star(star_size)
            turtle.penup()
            turtle.back(star_distance*(j+1))

#star(10)
galaxy(7,7)
time.sleep(1)