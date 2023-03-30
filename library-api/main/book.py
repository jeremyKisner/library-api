class Book:

    def __init__(self, name, read):
        self.name = name
        self.read = read

    def get_name(self):
        return self.name

    def get_read(self):
        return self.read

    def set_read(self):
        if self.get_read():
            self.read = 0
        else:
            self.read = 1
