from database_interator import DatabaseInterator

class DatabaseInterable:
    def __init__(self, sql_connector, query_template):
        self.db = sql_connector
        self.query_template = query_template

    def get_page(self, page):
        self.db.get(query=self.query_template, page=page)

    
    def __iter__(self):
        """Aqui iniciamos a iteração, retornando um objeto DatabaseIterator
        como Iterador."""
        return DatabaseInterator(self.db)

db = "SQL FAKE CONNECTION"
post_page_query_template = "SELECT * FROM db"

post_paginator = DatabaseInterable(db, post_page_query_template)

for page in post_paginator:
    #Do somethin with page
    for post in page:
        print(post['title'])