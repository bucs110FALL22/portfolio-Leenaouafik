import pygame
import random 
import math 
pygame.init()
window = pygame.display.set_mode()

screen_width= pygame.display.get_window_size()[0]
screen_length= pygame.display.get_window_size()[1]
print(pygame.display.get_window_size())
color_1= (0,0,139)
center= (400,300)
pygame.draw.circle(window,color_1, center,200)
pygame.display.flip()

#Part B
color_2= (0,0,0)
center_2= (800,300)
end_pos= (200,300)
pygame.draw.line(window,color_2, center_2, end_pos)
pygame.display.flip()

center_3= (400,600)
end_pos2= (400, 150)
pygame.draw.line(window, color_2, center_3, end_pos2)
pygame.display.flip()

#part b 
darts= random.randrange(0,screen_width)
darts_2 = random.randrange (0,screen_length)
print(darts)
print(darts_2)

col_red= (255,0,0)
pygame.draw.circle(window,col_red, center,15)
pygame.display.flip()
x1= 400
y1= 300 
x2= 520 
y2= 457 
width= 520 
distance_from_center = math.hypot(x1-x2, y1-y2)
is_in_circle = distance_from_center <= width/2 

#for i in range(10):
