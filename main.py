import requests

URL = "https://parkingapps.ucr.edu/spaces/"
r = requests.get(URL)
print(r.content)