import requests
# import json

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "e76965d853e439fea2c006d1e2545908"
city = input("Syötä kaupunki: ")

url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric&lang=fi"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response['main']['temp']
        description = json_response['weather'][0]['description']
        print(f"{city}\n"
              f"Lämpötila: {temp}°C\n"
              f"Sää: {description}")
except requests.exceptions.RequestException as e:
    print("hakua ei voitu suorittaa")

# miten voisi tehdä virheellisen inputin errorin :(