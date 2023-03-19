class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        dictionary = {'name': name, 'price': price}
        self.items.append(dictionary)
    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total += item['price']
        return total
loja = Store('carro')

print(loja.add_item('carro', 27))
print(loja.items)
print(loja.stock_price())


class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, type, weight):
        self.name = name
        self.type = type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.type}, {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight+100)

book = Book.hardcover("harry potter",1500)
print(Book.TYPES)
print(book)
