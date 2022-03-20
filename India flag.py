import turtle
flag = turtle.Turtle()

flag.speed(3)
flag.pensize(5)
flag.color('#054187')
flag.color('#000080')

def draw(x, y):
    flag.penup()
@@ -25,9 +25,10 @@ def draw(x, y):
draw(0, -80)
flag.circle(80, 360)

draw(0,-90)

#Green Rectangle
flag.color('green')
flag.color('#138808')
flag.begin_fill()

flag.forward(350)
@@ -44,8 +45,8 @@ def draw(x, y):


#Orange Rectangle
flag.color('orange')
draw(-350,80)
flag.color('#FF9933')
draw(-350,90)

flag.begin_fill()

@@ -60,4 +61,6 @@ def draw(x, y):

flag.end_fill()

turtle.done() 
flag.hideturtle()

turtle.done()