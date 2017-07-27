from turtle import *
speed(-1)
shape("turtle")
for side_n in range(3,7):
    if side_n%2==0:
        color("red")
    else:
        color("blue")
    for _ in range (side_n):
        forward(100)
        left(360/side_n)
    
