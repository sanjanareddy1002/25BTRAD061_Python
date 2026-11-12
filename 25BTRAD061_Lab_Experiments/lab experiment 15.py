class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(self.title, "issued successfully")
        else:
            print(self.title, "is not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.title, "returned successfully")
        else:
            print(self.title, "was not issued")

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)


book1 = Book("Python Programming", "John")

book1.display()
book1.issue_book()
book1.issue_book()
book1.return_book()
book1.display()
