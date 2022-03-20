import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 80
h = 0
for i in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    t.width((2*30)/100 + 1)
    h+= 1/n
    t.color(c)
    t.left(104)
    t.forward(i*3)
    for j in range(3):
        t.left(9)
        t.forward(i*2)
        t.left(42)
turtle.done