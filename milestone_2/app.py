from utils.database import *

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_books()
        elif user_input == "r":
            prompt_read_book()
        elif user_input == "d":
            prompt_delete_book()
        else:
            print("Invalid entry. Please enter a valid choice.")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    title = input("""
    To add a book, please add the title and author of the book.
    Title: """)
    author = input("""
    Thank you, now please add the author.
    Author: """)
    add_book(title, author)


def list_books():
    books = get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['title']} by {book['author']}, read: {read}")


def prompt_read_book():
    title = input('Enter the name of the book you just finished reading: ')
    mark_book_as_read(title)


def prompt_delete_book():
    title = input('Enter the name of the book you would like to remove: ')
    delete_book(title)


menu()
