import pandas as pd
import matplotlib.pyplot as plt

# Constants for file names
INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales.csv"


class Book:
    def __init__(self, book_id, title, author, genre, price, stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, quantity):
        self.stock += int(quantity)

    def __str__(self):
        return f" {self.title},  by  {self.author}  (ID: {self.book_id})"

    def to_dict(self):
        return self.__dict__  # turns books into a dictionary


class Inventory:
    def __init__(self):
        self.books = {}  # Using a dictionary for faster lookups by book_id

    def load_books(self):

        df = pd.read_csv(INVENTORY_FILE)
        df.drop_duplicates(inplace=True)
        for _, row in df.iterrows():
            book = Book(*row)  # unpacking the row as arguments
            self.books[book.book_id] = book
        print(f"Loaded {len(self.books)} books from {INVENTORY_FILE}")

    def save_books(self):
        df = pd.DataFrame([book.to_dict() for book in self.books.values()])
        df.to_csv(INVENTORY_FILE, index=False)
        print(f"Saved inventory to {INVENTORY_FILE}")

    def add_book(self, book):
        if book.book_id in self.books:
            print("Error: Book with this ID already exists.")
            return
        self.books[book.book_id] = book

    def find_book(self, book_id):
        book = self.books.get(book_id)
        return book

    def display_inventory(self):
        if not self.books:
            print("Inventory is empty.")
            return
        for book in self.books.values():
            print(book)


class Sales:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, book, quantity):
        self.transactions.append({
            "Book ID": book.book_id,
            "Title": book.title,
            "Quantity": int(quantity),
            "Total": book.price * int(quantity)
        })

    def save_transactions(self):
        df = pd.DataFrame(self.transactions)
        df.to_csv(SALES_FILE, index=False)
        print(f"Saved sales data to {SALES_FILE}")

    def load_transactions(self):

        self.transactions = pd.read_csv(SALES_FILE).to_dict(orient="records")
        print(f"Loaded {len(self.transactions)} sales transactions from {SALES_FILE}")

    def display_sales_data(self):
        df = pd.DataFrame(self.transactions)
        if df.empty:
            print("No sales data available.")
            return

        print(df)
        sales_by_title = df.groupby("Title")["Total"].sum()
        sales_by_title.plot(kind="barh")
        plt.title("Total Sales")
        plt.ylabel("Sales by Book")
        plt.show()

    def display_genre_sales_data(self):
        df = pd.DataFrame(self.transactions)
        if df.empty:
            print("No sales data available.")
            return

        sales_by_title = df.groupby("Genre")["Total"].sum()
        sales_by_title.plot(kind="pie")
        plt.title("Genre sales")
        plt.legend(title="Genres")
        plt.show()


inventory = Inventory()
sales = Sales()

inventory.load_books()
sales.load_transactions()

while True:
    print("\nBookshop Management System")
    print("1. Display Inventory")
    print("2. Add Book")
    print("3. Update Stock")
    print("4. Process Sale")
    print("5. View Sales Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display_inventory()

    elif choice == "2":
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")
        price = float(input("Enter the price: "))
        stock = int(input("Enter Stock: "))
        new_book = Book(book_id, title, author, genre, price, stock)
        inventory.add_book(new_book)

    elif choice == "3":
        book_id = int(input("Enter Book ID to update: "))
        book = inventory.find_book(book_id)
        if book:
            quantity = int(input("Enter quantity to add: "))
            book.update_stock(quantity)
        else:
            print("Book not found!")

    elif choice == "4":
        book_id = int(input("Enter Book ID to sell: "))
        book = inventory.find_book(book_id)
        if book:
            quantity = int(input("Enter quantity to sell: "))
            if quantity <= book.stock:
                book.update_stock(-quantity)
                sales.add_transaction(book, quantity)
            else:
                print("Insufficient stock!")
        else:
            print("Book not found!")

    elif choice == "5":
        sales.display_genre_sales_data()
        sales.display_sales_data()

    elif choice == "6":
        inventory.save_books()
        sales.save_transactions()
        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
