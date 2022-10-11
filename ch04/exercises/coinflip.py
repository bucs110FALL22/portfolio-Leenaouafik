import turtle
import random

my_turtle= turtle.Turtle()
window= turtle.Screen()

my_turtle.shape('turtle')
dist= 50 
angle= 90 
in_screen= True

while in_screen:
    coin = random.randrange(0, 2)
    if coin:           
        my_turtle.right(angle)
    else:                      
        my_turtle.left(angle)
    my_turtle.forward(dist)