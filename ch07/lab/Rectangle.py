class Rectangle: 
  def __init__(self, x, y, h, w):
    self.x= x
    self.y= y
    self.height= h
    self.width = w 

  def __str__(self): 
   return f'Rectangle({self.x},{self.y},{self.height},{self.width})'
    
    