import requests
import json

city = "Seoul"
apikey = "f3ed5a84ece8020fb14cc0002ef18cf1"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

print(type(result.text))
print(type(data))