import requests
from parsel import Selector

# 4
URL_BASE = "http://books.toscrape.com/catalogue/"

response = requests.get(URL_BASE + "the-grand-design_405/index.html")
selector = Selector(text=response.text)

title = selector.css(".product_main > h1::text").get()
price = selector.css(".price_color::text").re_first(r"£\d+\.\d{2}").replace("£", "")
description = selector.css("#product_description ~ p::text").get()
image = URL_BASE + selector.css(".item img::attr(src)").get()
available = selector.css(".product_main .availability::text").re_first("\d")

suffix = "...more"
if description.endswith(suffix):
    description = description.removesuffix(suffix)
    
print(title, price, description, image, available, sep=",")