import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"title": "hello", "content": "hello world", "price": 123}) # i can pass my own json data content type being json application
# get_response = requests.get(endpoint ,data={"query": "hello world from my data"}) # content type being http form encoded again

#print(get_response.text) # print text response
#print(get_response.status_code) # print the status code 
print(get_response.json()) # print json response