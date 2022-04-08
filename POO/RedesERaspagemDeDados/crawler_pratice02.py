import requests
from parsel import Selector

response = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers",
    headers={"User-agent": "Mozilla", "Accept": "text/html"},
).text

assert "bot detected" not in response

print(response)