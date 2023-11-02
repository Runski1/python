from tabulate import tabulate


class Publication:
    def __init__(self, name):
        self.name = name

    def print_properties(self):
        aliases = {"name": "Name", "author": "Author", "pagecount": "Pages", "editor_in_chief": "Editor-in-Chief"}
        publication_data = vars(self)
        for key, value in publication_data.items():
            if key in aliases:
                print(f"{aliases[key]}: {value}")
            else:
                print(f"{key}: {value}")


class Book(Publication):
    def __init__(self, name, author, pagecount):
        super().__init__(name)
        self.author = author
        self.pagecount = pagecount


class Magazine(Publication):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief


book = Book("Hytti n:o 6", "Rosa Liksom", 200)
book.print_properties()
magazine = Magazine("Aku Ankka", "Aki Hyyppä")
magazine.print_properties()
