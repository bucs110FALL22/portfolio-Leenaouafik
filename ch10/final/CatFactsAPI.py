import requests 
import json 

class CatFactsAPI: 
  def __init__(self, amount=2):
    self.url= "https://cat-fact.herokuapp.com"
    
  def get(self): 
    facts= "/facts/random?animal_type=cat&amount=2"
    response= requests.get(self.url + facts)
    print (response.json())
