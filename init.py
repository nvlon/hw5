import turtle
# impport  colorsys
t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.pencolor('yellow')
t.penup()
t.goto(0,200)
t.pendown()
t.speed(0)

a=0
b=0

while True:
    t.forward(a)
    t.right(b)
    a +=3
    b +=1
    if b == 200:
        break

t.hideturtle()
turtle.done ()


















