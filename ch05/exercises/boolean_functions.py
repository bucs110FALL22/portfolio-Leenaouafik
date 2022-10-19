def percentage_to_letter(score=0):
  scores= int(score)
  if scores >= 90: 
    return 'A' 
  elif scores >=80: 
    return 'B'
  elif scores >=70:
    return 'C'
  elif scores >=60: 
    return 'D'
  elif scores <60: 
    return 'F'


score =int(input("What is your score?:"))
percentage_to_letter(score)