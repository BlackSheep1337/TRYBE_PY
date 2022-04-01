import json
import csv


def retrieve_books(file):
    return [json.loads(line) for line in file]


def count_books_by_category(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1
    return categories


def calculate_percentage_by_category(number_of_books, book_count_by_category):
    return [
        [category, num_books / number_of_books]
        for category, num_books in book_count_by_category.items()
    ]


def write_csv_report(file, header, rows):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

if __name__ == '__main__':
    with open('books.json') as file:
       books = retrieve_books(file)
    book_count_by_category = count_books_by_category(books)

    number_of_books = len(books)
    books_percentage_rows = calculate_percentage_by_category(
        number_of_books, book_count_by_category
    )

    header = ["categoria", "porcentagem"]
    with open("report.csv", "w") as file:
        write_csv_report(file, header, books_percentage_rows)