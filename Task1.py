# Base Class
class Person:
    def __init__(self, name):
        self.name = name


# Derived Class (Inheritance)
class Member(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__borrowed_books = []   # Encapsulation

    def borrow_book(self, book):
        self.__borrowed_books.append(book)
        print(f"{self.name} borrowed '{book}'.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            print(f"{self.name} returned '{book}'.")
        else:
            print("Book not found in borrowed list.")

    def show_books(self):
        if self.__borrowed_books:
            print("Borrowed Books:")
            for book in self.__borrowed_books:
                print("-", book)
        else:
            print("No books borrowed.")


# Library Class
class Library:
    def __init__(self):
        self.books = ["Python Basics", "Data Structures", "Machine Learning"]

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print("-", book)

    def issue_book(self, member, book):
        if book in self.books:
            self.books.remove(book)
            member.borrow_book(book)
        else:
            print("Book is not available.")

    def accept_return(self, member, book):
        member.return_book(book)
        self.books.append(book)


# Main Program
library = Library()
name = input("Enter your name: ")
member = Member(name)

while True:
    print("\n===== Library Menu =====")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. My Borrowed Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        library.display_books()
        book = input("Enter book name: ")
        library.issue_book(member, book)

    elif choice == "3":
        book = input("Enter book name to return: ")
        library.accept_return(member, book)

    elif choice == "4":
        member.show_books()

    elif choice == "5":
        print("Thank you for using the Library System!")
        break

    else:
        print("Invalid choice! Please try again.")
