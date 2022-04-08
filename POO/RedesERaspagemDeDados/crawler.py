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
            price = product.css(".product_price .price_color::text").re(r"£\d+\.\d{2}")[0]
            # file.writelines(f"{title} - {price}")
            # file.write("\n")
            print(title, price)

            detail_href = selector.css('h3 a::attr(href)').get()
            detail_page_url = URL_BASE + detail_href

            detail_response = requests.get(detail_page_url)
            detail_selector = Selector(text=detail_response.text)

            description = detail_selector.css('#product_description ~ p::text').get()
            suffix = '...more'
            if description.endswith(suffix):
                description = description[:-len(suffix)]
            print(description)

        next_page_url = selector.css(".next a::attr(href)").get()
    # Descobre qual é a próxima página