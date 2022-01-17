import turtle
t = turtle.Turtle()
S = turtle.Screen()
S.bgcolor('black')
t.speed(10)
turtle.color=('yellow','pink','white','light blue')
c=0
#Pranav_Khemani
for i in range(50):
    t.forward(i*10)
    t.right(144)
    t.color(turtle.color[c])
    if c==3:
        c=0
    else:
        c+=1