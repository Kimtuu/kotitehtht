import requests

# import json

req = "https://api.chucknorris.io/jokes/random"

joke = requests.get(req).json()

# tsekkasin tällä↓ dumpin avaimen ja arvon :)
# print(json.dumps(joke, indent=1))

print(joke["value"])




