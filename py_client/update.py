import requests



endpoint = "http://localhost:8000/api/products/4/update/"

data ={
    "title": "proddd4",
    "price": 4.5
}
get_response = requests.put(endpoint, json=data)
print(get_response.json()) 