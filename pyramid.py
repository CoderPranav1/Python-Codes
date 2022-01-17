import turtle
import colorsys
#Made By Coder.Pranav
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 190
h = 30
t.left(180)
for i in range(180):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h+= 1/n
    t.color(c)
    t.left(1350)
    t.forward(i*7)