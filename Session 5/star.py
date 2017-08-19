from turtle import *
shape ("turtle")
speed(-1)
left(36.5)
def draw_star(x,y,l):
    penup()
    setpos(x,y)
    pendown()
    for i in range (5):
        forward(l)
        left(144)

color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(30, 100)
    draw_star(x, y, length)
