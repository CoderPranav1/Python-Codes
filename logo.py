import turtle

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')

t.color('light blue')
t.begin_fill()
t.left(45)
t.forward(50)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.end_fill

t.right(90)
t.forward(50)

t.color('blue')
t.begin_fill()
t.right(360)
t.left(90)
t.back(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.end_fill

t.color('dark blue')
t.begin_fill()
t.left(45)
t.forward(50)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.end_fill


s.exitonclick()