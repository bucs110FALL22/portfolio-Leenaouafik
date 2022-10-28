import turtle

def mikesears(): 
 ears= turtle.Turtle()
 ears.penup()
 ears.goto(-85,120)
 ears.pendown()
 for i in range(180):
  ears.forward(1)
  ears.right(1)
 ears.right(90)
 ears.forward(115) 

def mikesears2(): 
 ears_2= turtle.Turtle()
 ears_2.penup()
 ears_2.goto(35,10)
 ears_2.pendown()
 for i in range(180):
  ears_2.forward(1)
  ears_2.left(1)
 ears_2.left(90)
 ears_2.forward(115)

def backface(): 
 turtle.bgcolor("lightblue")
 turtle.shape("circle")
 turtle.shapesize(12)
 turtle.fillcolor("lightgreen")

def mike(): 
 mike= turtle.Turtle()
 mike.goto(0,40)
 mike.shape("circle")
 mike.shapesize(9.5,6,2)
 mike.left(90)
 mike.fillcolor("white")

def eye(): 
 eye= turtle.Turtle()
 eye.penup()
 eye.goto(0,40)
 eye.shape("circle")
 eye.shapesize(3)
 eye.fillcolor("green")


def pupil():
 pupil=turtle.Turtle()
 pupil.penup()
 pupil.goto(0,40)
 pupil.shape("circle")

def smile(): 
 smile= turtle.Turtle()
 smile.penup()
 smile.goto(-70,-75)
 smile.pendown()
 for i in range(4):
  smile.forward(40)
  smile.left(7)

def main(): 
  mikesears()
  mikesears2()
  backface()
  mike()
  eye()
  pupil()
  smile()
main()