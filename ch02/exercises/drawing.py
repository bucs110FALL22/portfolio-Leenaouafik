import turtle 
my_turtle= turtle.Turtle()
wn= turtle.Screen()
my_turtle.shape('turtle')
my_turtle.color("pink")
num_sides= int(input("Please input the number of sides: "))
length= int(input("Please input the length of sides:"))
for i in [1]*num_sides: 
  my_turtle.left(360/num_sides)
  my_turtle.forward(length)