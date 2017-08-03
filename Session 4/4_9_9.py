from turtle import *

shape("turtle")
left(36.5)

def draw_a_star(sz):
    """Draw a star where the length of each side is 100 units."""
    angle = 144
    for i in range (5):
        forward(sz)
        left(angle)
      
    return
draw_a_star(100)



