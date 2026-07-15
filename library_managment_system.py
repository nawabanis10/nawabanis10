class Books:
    total_books=0
    library_name="City Library"

    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.__price=price
        Books.total_books+=1

    def display_book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.__price}")

    @classmethod
    def display_library_info(cls):
        print(f"Library Name: {cls.library_name}, Total Books: {cls.total_books}")

    def update_book_price(self,new_price):
        self.__price=new_price
        print(f"Price of '{self.title}' updated to ${self.__price}")

    def borrow_book(self):
        if self.total_books < 3:
            print(f"You have borrowed '{self.title}' by {self.author}. Please return it on time.")

    def return_book(self):
        if self.total_books == 0:
            print(f"You have returned '{self.title}' by {self.author}. Thank you!")

    @classmethod
    def change_library_name(cls,new_name):
        cls.library_name=new_name
        print(f"Library name changed to {cls.library_name}")

    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        else:
            return False
        
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if self.is_valid_price(new_price):
            self.__price = new_price
            print(f"Price of '{self.title}' updated to ${self.__price}")
        else:
            print("Invalid price. Price must be greater than 0.")

b1=Books("python", "Guido van rossam", 10.99)
b2=Books("Java", "James Gosling", 12)
b3=Books("DSA", "George Orwell", 13.5)

b1.display_book_info()
b2.display_book_info()
b3.display_book_info()

Books.display_library_info()
# Books.total_books()

b1.update_book_price(15.99)
b2.update_book_price(14.5)
b3.update_book_price(16.75)

b1.borrow_book()
# b2.borrow_book()
# b3.borrow_book()

# b1.return_book()
b2.return_book()
# b3.return_book()

Books.change_library_name("Downtown Library")

b1.is_valid_price(15.99)
b2.is_valid_price(-5)
b3.is_valid_price(0)

b1.get_price()
b2.get_price()
b3.get_price()


