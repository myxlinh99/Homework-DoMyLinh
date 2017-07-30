from turtle import *
shape ("turtle")
speed (-1)

colors = ["red", "blue", "purple", "yellow", "turquoise"]
 
from turtle import *
speed(-1)
for side_n in range (3,8):
    color(colors[side_n-3])
    for a in range (side_n):
        forward (100)
        left (360/side_n)
