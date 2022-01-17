import turtle
import colorsys

t=turtle.Turtle
s=turtle.Screen() .bgcolor("black")
turtle.color("white")
turtle.speed(0)
turtle.width(5)
n=200
h=0
for i in range (200):
    turtle.right(59)
    for c in range (1):
        turtle.forward(i*2)
        c=colorsys.hsv_to_rgb(h,1,0.8)
        h += 1/n
        turtle.color(c)

turtle.exitonclick                