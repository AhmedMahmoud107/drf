import requests



endpoint = "http://localhost:8000/api/products/10/delete"


get_response = requests.delete(endpoint)

get_response.status_code == 204
print(get_response.status_code) 