import turtle
wn= turtle.Screen()

    
turtle.color("orange")
turtle.pendown()
for turn in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    turtle.left(turn)
    turtle.forward(100)
print(turtle.position())