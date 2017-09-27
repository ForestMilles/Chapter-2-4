import turtle
wn= turtle.Screen()

size=25
inverted=0
angle=144

turtle.color("blue")
turtle.penup()

turtle.pendown()

for i in range(5):
    turtle.forward(size*12)
    turtle.right(angle)