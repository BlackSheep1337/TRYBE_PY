# import requests
# from parsel import Selector

# titles = selector.css(".product_pod h3 a::attr(title)").getall()
# price = selector.css('.product_price .price_color::text').getall()

# for product in selector.css(".product_pod"):
#     with open('./reports/titles.txt', 'a') as file:
#         title = product.css("h3 a::attr(title)").get()
#         price = product.css(".price_color::text").get()
#         file.writelines(f"{title} - {price}")
#         file.write("\n")


# for product in selector.css(".product_pod"):
#     title = product.css("h3 a::attr(title)").get()
#     price = product.css(".price_color::text").get()
#     print(title, price)

from parsel import Selector
import requests


# Define a primeira página como próxima a ter seu conteúdo recuperado
URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'
while next_page_url:
    # Busca o conteúdo da próxima página
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    # Imprime os produtos de uma determinada página
    with open("./reports/product_reports.txt", 'a') as file:
        for product in selector.css(".product_pod"):
            title = product.css("h3 a::attr(title)").get()
            price = product.css(".price_color::text").get()
            # file.writelines(f"{title} - {price}")
            # file.write("\n")
            print(title, price)
        next_page_url = selector.css(".next a::attr(href)").get()
    # Descobre qual é a próxima página