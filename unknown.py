import turtle
import colorsys
#Made By Coder.Pranav
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('Black')
t.speed(0)
n = 360
h = 180
t.right(180)
for i in range(180):
    c = colorsys.hsv_to_rgb(h, 0.8, 0.9)
    h+= 7/n
    t.color(c)
    t.right(62778)
    t.forward(i*5)