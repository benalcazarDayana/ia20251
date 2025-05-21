class Vehicle:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def printingMessage(self):
        return f"The model is {self.model} and its maker is {self.maker}"

class Car(Vehicle):
    def __init__(self, maker, model, doors):
        super().__init__(maker, model)
        self.doors = doors

    def infoPrinting(self):
        return f"The maker is {self.maker}, the model is {self.model} and has {self.doors} doors"

class Truck(Vehicle):
    def __init__(self, maker, model, weight):
        super().__init__(maker, model)
        self.weight = weight

    def infoPrinting(self):
        return f"The maker is {self.maker}, the model is {self.model} and has {self.weight} weight"

# Crear objetos correctamente
vehicleObject = Vehicle('Generic', 'modelTX')
carObject = Car('Toyota', 'Yaris', 3)
truckObject = Truck('Hino', 'GH', 120)

# Imprimir información
print(vehicleObject.printingMessage())
print(carObject.infoPrinting())
print(truckObject.infoPrinting())


print('----------------------------------------------------------------------')

# Clase base para libros
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def info_printing(self):
        status = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"


# Clase Library que administra una colección de libros
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def lend_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"Book '{title}' lent successfully.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' is not in the library or already available.")

    def list_available(self):
        print("\nAvailable books:")
        for book in self.books:
            if book.available:
                print(book.info_printing())
        print()


# Subclase para libros electrónicos
class EBook(Book):
    def __init__(self, title, author, file_format, available=True):
        super().__init__(title, author, available)
        self.file_format = file_format

    def info_printing(self):
        status = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Format: {self.file_format}, Status: {status}"


# Crear una biblioteca y añadir libros
my_library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
ebook1 = EBook("Python for Beginners", "John Doe", "PDF")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(ebook1)

# Mostrar libros disponibles
my_library.list_available()

# Préstamo de libros
my_library.lend_book("1984")
my_library.list_available()

# Devolver libros
my_library.return_book("1984")
my_library.list_available()