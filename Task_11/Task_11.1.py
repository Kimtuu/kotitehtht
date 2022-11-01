class Release:
    def __init__(self, release_name):
        self.release_name = release_name

    def print_info(self):
        print(self.release_name)


class Book(Release):
    def __init__(self, writer, pages, release_name):
        self.writer = writer
        self.pages = pages
        super().__init__(release_name)

    def print_info(self):
        super().print_info()
        print(f"writer: {self.writer}, pages: {self.pages}")


class Tabloid(Release):
    def __init__(self, chief_editor, release_name):
        self.chief_editor = chief_editor
        super().__init__(release_name)

    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.chief_editor}")


if __name__ == '__main__':
    kirja = Book("Rosa Liksom", 200, "Hytti n:o 6")
    kirja.print_info()
    lehti = Tabloid("Aki Hyyppä", "Aku Ankka")
    lehti.print_info()
