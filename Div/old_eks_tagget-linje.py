import turtle
turtle.setup(500,500,100,100)
# Lag tagget linje med turtle graphics
def turt_tagger(size, number):
    turtle.left(45)
    for i in range(number):
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
    turtle.right(45)

for l in range(4):
    turt_tagger(12,7)
    turtle.right(90)