article= "Giant Backfire Trumps Demand for Special Master is Looking like a Mistake"



substiutions=(
  "Trumps" : "Homer Simpsons"
  "Special Master" : "Donuts"
)

for key, value  in substitions.items():
  article = article.replace(key,value)

print(article)