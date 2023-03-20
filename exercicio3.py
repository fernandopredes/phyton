class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        new_store = Store(store.name + " - franchise")
        return new_store

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name}, total stock price: {int(store.stock_price())}"


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print(Store.store_details(store2))

#composition example

class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

class Book():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book('Harry Potter')
book2 = Book('Exorcist')
shelf = Bookshelf(book, book2)

print(shelf)
print(shelf.books)
