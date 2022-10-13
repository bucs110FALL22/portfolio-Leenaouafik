import turtle 


def drawEqShape(my_turtle, num_sides=0, side_length=0): 
  for i in range(6): 
    my_turtle.forward(side_length)
    my_turtle.right(360/num_sides)

num_sides= int(input("enter the number of sides:"))
side_length= int(input("enter the length:"))

mturtle= turtle.Turtle()
mturtle.shape('turtle')
mturtle.color('green')
drawEqShape(mturtle,num_sides,side_length)