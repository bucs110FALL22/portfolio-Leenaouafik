import requests 
import json 

class DogFactsAPI: 
  def __init__(self): 
    self.url= "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=2"
   
  def get(self): 
    response= requests.get(self.url)
    print(response)