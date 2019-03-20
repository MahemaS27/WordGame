import requests
import json

app_id = "6ce9309d"
app_key = "b815139ed48d09f44ffb8f7c7a66a0bf"

language = 'en'
word_id = 'selfie'

url = "https://od-api.oxforddictionaries.com/api/v1" + language + "/" + word_id.lower()

r = requests.get(url)

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n"+ json.dumps(r.json()))