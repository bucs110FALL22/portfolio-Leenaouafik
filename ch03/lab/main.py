import turtle #1. import modules
import random
import pygame 
import math 

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.down ()
leonardo.down()
distance= random.randrange(0,11)
distance_2= random.randrange(0,11)
for i in range (10): 
  michelangelo.forward(distance)
  leonardo.forward(distance_2)

michelangelo.up()
michelangelo.goto(-100,20)  
leonardo.up()
leonardo.goto(-100,-20)
# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

color= (100,149,237)
wind_col= (255,248,220)

num_sides= 3
side_length= 50
coords= []
offset= 0
for i in range(num_sides):
  theta = (2.0 * math.pi * i / num_sides)
  x= side_length * math.cos(theta) + offset 
  y= side_length * math.sin(theta) + offset
  coords_tri= (x,y)
  coords.append(coords_tri)
pygame.draw.polygon(window, color, coords)
pygame.display.flip()
pygame.time.delay(500)
window.fill(wind_col)
pygame.display.flip()


num_sides2= 4
coords_2= []
for i in range(num_sides2): 
  theta= (2.0*math.pi*i/num_sides2)
  x= side_length*math.cos(theta)+offset
  y=side_length * math.sin(theta)+offset
  coords_square= (x,y)
  coords_2.append(coords_square)
pygame.draw.polygon(window, color, coords_2)
pygame.display.flip()
pygame.time.delay(500)
window.fill(wind_col)
pygame.display.flip()

num_sides3= 6
coords_3= []
for i in range(num_sides3):
  theta= (2.0*math.pi*i/num_sides3)
  x= side_length*math.cos(theta)+offset
  y= side_length*math.sin(theta)+offset
  coords_hex= (x,y)
  coords_3.append(coords_hex)
pygame.draw.polygon(window, color, coords_3)
pygame.display.flip()
pygame.time.delay(500)
window.fill(wind_col)
pygame.display.flip()

num_sides4= 9
coords_4=[]
for i in range(num_sides4): 
  theta= (2.0*math.pi*i/num_sides4)
  x= side_length*math.cos(theta)+offset
  y= side_length*math.sin(theta)+offset
  coords_non= (x,y)
  coords_4.append(coords_non)
pygame.draw.polygon(window, color, coords_4)
pygame.display.flip()
pygame.time.delay(500)
window.fill(wind_col)
pygame.display.flip()

num_sides5= 360
coords_5=[]
for i in range(num_sides5):
  theta= (2.0*math.pi*i/num_sides5)
  x= side_length*math.cos(theta)+offset
  y= side_length*math.sin(theta)+offset
  coords_circ=(x,y)
  coords_5.append(coords_circ)
pygame.draw.polygon(window, color, coords_5)
pygame.display.flip()
pygame.time.delay(500)
window.fill(wind_col)
pygame.display.flip()