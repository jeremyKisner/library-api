class Book:

    def __init__(self, record):
        self.name = record["name"]
        self.author = record["author"]
        self.type = record["type"]
        self.isbn_13 = record["isbn_13"]
        self.isbn_10 = record["isbn_10"]
        self.published = record["published"]
        self.publisher = record["publisher"]
        self.copies = record["copies"]

    def get_name(self):
        return self.name
