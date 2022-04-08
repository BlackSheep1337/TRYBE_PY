from parsel import Selector
import requests

# URL_BASE = 'https://books.toscrape.com/catalogue/'
# page_base_url = 'page-1.html'

# response = requests.get(URL_BASE + page_base_url)
# selector = Selector(text=response.text)

# href = selector.css(".product_pod h3 a::attr(href)").get()

# desc_response = requests.get(URL_BASE + href)

# desc_selector = Selector(text=desc_response.text)

# description = desc_selector.css('.product_page > p::text').get()

# print(description)

# URL_BASE = 'https://books.toscrape.com/'

# response = requests.get(URL_BASE)

# selector = Selector(text=response.text)

# prices = selector.css('.price_color::text').re(r"£\d+\.\d{2}")

# total = 0
# for price in prices:
#     remove_euro = price.replace("£", "")
#     total += float(remove_euro)
#     media = total / len(prices)

# print(total)
# print(media)

# response = requests.get("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
# selector = Selector(text=response.text)

# description = selector.css('#product_description ~ p::text').get()

# suffix = "...more"
# if description.endswith(suffix):
#     description = description.removesuffix(suffix)

# print(description)

string1 = "Welcome to python 3.9"
print("Original String 1 : ", string1)

result = string1.removesuffix('3.9')
print("New string : ", result)

string2 = "Welcome Geek"
print("Original String 2 : ", string2)
  
# suffix doesn't exist
result2 = string2.removesuffix("Welcome")
print("New string : ", result2)