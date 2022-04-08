from parsel import Selector
import requests

#1
BASE_URL = 'https://httpbin.org/encoding/utf8'

response = requests.get(BASE_URL)
selector = Selector(text=response.text)
# print(response.text)

#2
response = requests.get('https://api.github.com/users').json()

for user in response: print(f"{user['login']} - {user['url']}")