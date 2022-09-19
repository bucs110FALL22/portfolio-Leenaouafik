import random 
my_nums= random.randrange(1,11)
num_guesses= 0

for i in range[3]: 
  guess= int(input("Guess a number:"))
  if result > guess: 
    print("too low")
  else: 
    print ("too high")
  if result == guess: 
    print("correct!")