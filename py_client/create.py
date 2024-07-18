import requests


endpoint = "http://localhost:8000/api/products/"

data ={
    "title": "prod8",
    "price": 18.17 ,
}

get_response = requests.post(endpoint ,json=data)
print(get_response.json()) 