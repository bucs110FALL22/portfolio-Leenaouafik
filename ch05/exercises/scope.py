def myfunc(mynum,mynum_2):
  result= 0
  for i in range (mynum_2): #runs the code mynum times
    result= result+mynum
  return result 

def main():
  res = myfunc(5, 2)
  print(res)
  res = myfunc(3, 4)
  print (res)

main()      #basically first line of code 

def myexp(num,exp):
  result=1
  for i in range (exp):
    result= result*num
  return result 

def main():
  resu= myexp(4,2)
  print(resu)
  resu= myexp(3,2)
  print (resu)

main()

def square(nums): 
  return myfunc + nums