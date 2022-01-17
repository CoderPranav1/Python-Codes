import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 190
h = 90
t.right(180)
for i in range(180):
    c = colorsys.hsv_to_rgb(h, 0.8, 0.9)
    h+= 7/n
    t.color(c)
    t.right(62778)
    t.forward(i*5)