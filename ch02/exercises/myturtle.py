import turtle 
my_turtle= turtle.Turtle()
my_turtle.shape("turtle")
turtle.color ("purple")
num_sides= int(input("Please input the number of sides: "))
length= 50
angle= 360/num_sides
for i in [angle]*num_sides: 
  my_turtle.forward(length)
  my_turtle.left(i)