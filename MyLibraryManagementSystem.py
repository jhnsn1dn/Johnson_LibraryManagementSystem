from abc import ABC, abstractmethod

# Abstract class for Library Operations
class LibraryOperations(ABC):
    @abstractmethod
    def borrow(self, member, book):
        pass
    
    @abstractmethod
    def return_book(self, member, book):
        pass

# Book class
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_borrowed = False

    # Getters and Setters
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        self.__author = author
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def is_borrowed(self):
        return self.__is_borrowed

    def set_borrowed(self, status):
        self.__is_borrowed = status

# Subclass for different types of books
class Fiction(Book):
    def __init__(self, title, author, isbn,):
        super().__init__(title, author, isbn)

class NonFiction(Book):
    def __init__(self, title, author, isbn,):
        super().__init__(title, author, isbn)

class Poetry(Book):
    def __init__(self, title, author, isbn,):
        super().__init__(title, author, isbn)

class History(Book):
    def __init__(self, title, author, isbn,):
        super().__init__(title, author, isbn)

# Member class
class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    # Getters and Setters
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_member_id(self):
        return self.__member_id
    
    def set_member_id(self, member_id):
        self.__member_id = member_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        self.__borrowed_books.append(book)
        book.set_borrowed(True)
    
    def return_book(self, book):
        self.__borrowed_books.remove(book)
        book.set_borrowed(False)

# Subclass for different types of members
class PremiumMember(Member):
    def __init__(self, name, member_id, membership_level):
        super().__init__(name, member_id)
        self.__membership_level = membership_level

    def get_membership_level(self):
        return self.__membership_level
    
    def set_membership_level(self, membership_level):
        self.__membership_level = membership_level

# Librarian class
class Librarian:
    def __init__(self, name, librarian_id):
        self.__name = name
        self.__librarian_id = librarian_id

    # Getters and Setters
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_librarian_id(self):
        return self.__librarian_id
    
    def set_librarian_id(self, librarian_id):
        self.__librarian_id = librarian_id

    def manage_book(self, book, action):
        if action == "add":
            Library.add_book(book)
        elif action == "remove":
            Library.remove_book(book)

# Library class implementing LibraryOperations
class Library(LibraryOperations):
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)
    
    def remove_book(self, book):
        self.__books.remove(book)
    
    def add_member(self, member):
        self.__members.append(member)
    
    def remove_member(self, member):
        self.__members.remove(member)

    # Overriding abstract methods
    def borrow(self, member, book):
        if not book.is_borrowed():
            member.borrow_book(book)
            print(f"{member.get_name()} borrowed {book.get_title()}")
        else:
            print(f"{book.get_title()} is already borrowed")

    def return_book(self, member, book):
        if book in member.get_borrowed_books():
            member.return_book(book)
            print(f"{member.get_name()} returned {book.get_title()}")
        else:
            print(f"{member.get_name()} did not borrow {book.get_title()}")

# Demonstration of the Library Management System

# Create library instance
library = Library()

# Create book instances
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("Python Programming", "John Doe", "0987654321")

# Create member instances
member1 = Member("Alice", "M001")
premium_member1 = PremiumMember("Bob", "PM001", "Gold")

# Create librarian instance
librarian = Librarian("Eve", "L001")

# Librarian adds books to the library
librarian.manage_book(book1, "add")
librarian.manage_book(book2, "add")

# Library adds members
library.add_member(member1)
library.add_member(premium_member1)

# Members borrow books
library.borrow(member1, book1)
library.borrow(premium_member1, book2)

# Members return books
library.return_book(member1, book1)
library.return_book(premium_member1, book2)