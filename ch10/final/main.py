import random
import CatFactsAPI
import DogFactsAPI

def main():
  cats= CatFactsAPI.CatFactsAPI(amount=2)
  results = cats.get() 
  print (results)

  dogs= DogFactsAPI.DogFactsAPI()
  results= dogs.get()
  print(results)

main()