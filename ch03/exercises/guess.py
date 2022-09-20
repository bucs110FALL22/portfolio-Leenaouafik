import random 
my_nums= random.randrange(1,11)
correct_num= False


for i in range(5): 
  guess= int(input("Guess a number:"))
  if guess > my_nums:
    print("your guess too high")
  elif guess < my_nums:
    print("your guess is too low")
  else: 
    print("correct!")