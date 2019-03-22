import requests
import json



app_id = "6ce9309d"
app_key = "b815139ed48d09f44ffb8f7c7a66a0bf"



language = 'en'
target_language = "es"
word_id = 'orange'


#url Normalized frequency
definition_url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + language + '/' +word_id
r = requests.get(definition_url, headers = {'app_id' : app_id, 'app_key' : app_key})
status_code = ("code {}\n".format(r.status_code))
textfile = "text \n" + r.text
json_string=json.dumps(r.json(), indent =4, separators=(",", ":"))


data = json.loads(json_string)
print(data , '\n')


word = data['results'][0]["id"]
print ('word:', word)

