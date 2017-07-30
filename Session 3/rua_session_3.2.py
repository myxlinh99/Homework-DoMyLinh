from turtle import *
speed(-1)
shape("turtle")

colors = ["red", "blue", "brown", "yellow", "grey"]
i = 0
for i in range (5):
    
    color(colors[i])
    begin_fill()

    forward (50)
    left(90)
    forward(80)
    left (90)
    forward(50)
    left(90)
    forward(80)
    left(90)
    forward(50)
    i += 1
    end_fill()
