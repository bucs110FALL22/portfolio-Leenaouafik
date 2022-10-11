def star_pyramid():
  print("enter the number of rows")
  rows= int(input(":"))
  for i in range (rows):
    print("*"*i)
star_pyramid()

def rstar_pyramid():
  print("enter the number of rows")
  rows_2= int(input(":"))
  for i in range(rows_2,-1):
    print("*"*i)
star_pyramid()