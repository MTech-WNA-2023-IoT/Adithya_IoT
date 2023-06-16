import json
from urllib.request import urlopen
#Create user account and obtain API key from https://www.weatherapi.com

url = "https://api.weatherapi.com/v1/current.json?key=52935acb939f4725a2254508231606&q=kollam&aqi=no"

api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)
# data= json_api['currently']
print("New data")
print(json_api)

print("Parsed")
data=json_api["location"]
print(data)
