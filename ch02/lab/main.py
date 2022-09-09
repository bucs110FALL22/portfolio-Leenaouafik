import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week= 12
print(classes_per_week,int(classes_per_week))
cost_per_week= 480
print(cost_per_week,int(cost_per_week))
cost_per_class= cost_per_week/classes_per_week
print(cost_per_class,float(cost_per_class))
#Part B
my_list= ["homer", "marge", "bart", "lisa", "maggie"]
random.choice(my_list)
result= random.choice(my_list)
print(result)