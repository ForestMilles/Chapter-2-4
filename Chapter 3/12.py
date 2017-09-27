
import turtle
wn= turtle.Screen()

size = 100

turtle.color("blue")
fullsize=-(size+3*(size/10.0))
for i in range(12):
    turtle.penup()
    turtle.forward(size)
    turtle.pendown()
    turtle.forward(size/10.0)
    turtle.penup()
    turtle.forward(2*(size/10.0))
    turtle.stamp()
    turtle.forward(fullsize)
    turtle.right(30)