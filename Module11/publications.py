from tabulate import tabulate
class Publication:
    def __init__(self, name):
        self.name = name

    def print_properties(self):
        aliases = {"name": "Name", "author": "Author", "pagecount": "Pages", "editor_in_chief": "Editor-in-Chief"}
        publication_data = vars(self)
        pretty_publication_data = {}
        for key, value in publication_data.items():
            if key in aliases:
                pretty_publication_data.update({aliases[key]: value})
            else:
                pretty_publication_data.update({key: value})

        print(tabulate(pretty_publication_data, headers="keys", tablefmt="pretty"))



class Book(Publication):
    def __init__(self, name, author, pagecount):
        super().__init__(name)
        self.author = author
        self.pagecount = pagecount

    def print_properties(self):
        super().print_properties()


class Magazine(Publication):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def print_properties(self):
        super().print_properties()


book = Book("ASD", "Matias", 200)
book.print_properties()
magazine = Magazine("Aku Ankka", "Mikko Metelä")
magazine.print_properties()
