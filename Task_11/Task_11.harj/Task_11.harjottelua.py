class Publication:

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun nimi on: {self.name}")


class Magazine(Publication):

    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.editor}\n")


class Book(Publication):

    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Kirjailijan nimi: {self.author}\n"
              f"Sivumäärä: {self.page_count}\n")


pub1 = Magazine("Aku Ankka", "Aki hyyppä")
pub1.print_info()

pub2 = Book("Hytti n:o 6", "Rosa Liksom", "200")

pub2.print_info()
