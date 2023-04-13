class Book:

    def __init__(self, record):
        self.set_variables(record)

    def set_variables(self, record):
        if "name" in record:
            self.set_name(record["name"])
        if "author" in record:
            self.set_author(record["author"])
        if "type" in record:
            self.set_type(record["type"])
        if "isbn_13" in record:
            self.set_isbn_13(record["isbn_13"])
        if "isbn_10" in record:
            self.set_isbn_10(record["isbn_10"])
        if "published" in record:
            self.set_published(record["published"])
        if "publisher" in record:
            self.set_publisher(record["publisher"])
        if "copies" in record:
            self.set_copies(record["copies"])

    def get(self):
        return (
            self.get_name(),
            self.get_author(),
            self.get_type(),
            self.get_isbn_13(),
            self.get_isbn_10(),
            self.get_published(),
            self.get_publisher(),
            self.get_copies()
        )

    def get_name(self) -> str:
        return getattr(self, "name", "")

    def set_name(self, value):
        self.name = value

    def get_author(self) -> str:
        return self.author

    def set_author(self, value):
        self.author = value

    def get_type(self) -> str:
        return getattr(self, "type", "")

    def set_type(self, value):
        self.type = value

    def get_isbn_13(self) -> int:
        return int(self.isbn_13)

    def set_isbn_13(self, value):
        self.isbn_13 = value

    def get_isbn_10(self) -> int:
        return int(self.isbn_10)

    def set_isbn_10(self, value):
        self.isbn_10 = value

    def get_published(self) -> str:
        return self.published

    def set_published(self, value):
        self.published = value

    def get_publisher(self) -> str:
        return self.publisher

    def set_publisher(self, value):
        self.publisher = value

    def get_copies(self) -> int:
        return int(getattr(self, "copies", 0))

    def set_copies(self, value):
        self.copies = value
