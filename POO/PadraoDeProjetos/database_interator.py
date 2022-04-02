class DatabaseInterator:
    def __init__(self, sql_connector):
        """No construtor da classe iteradora definimos o valor inicial do
        contador current_page, e também o(s) atributo(s) que será(ão)
        responsável(is) por armazenar/acessar a coleção de dados pela qual
        queremos iterar."""
        self.db = sql_connector
        self.current_page = 0
    
    def __next__(self):
        """Este método busca no banco de dados a página que queremos e
        incrementa o contador current_page, para retornarmos a próxima página
        na próxima vez que o método for chamado."""

        data = self.interable.get_page(page=self.current_page)

        if not data:
            raise StopIteration()

        self.current_page += 1
        return data