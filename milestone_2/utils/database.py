from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from database

"""

books_file = 'books.json'


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text primary key, author text, read integer)')


def add_book(title, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))


#    books = get_all_books()
#   books.append({'title': title, 'author': author, 'read': False})
#    _save_all_books(books)


#  with open(books_file, 'a') as file:
#     file.write(f'{title},{author},0\n')
#    file.append({'title': title, 'author': author, 'read': False})


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books

    # with open(books_file, 'r') as file:
    #    return json.load(file)
    #    lines = [line.strip().split(',') for line in file.readlines()]


#  return [
#      {'title':line[0], 'author':line[1], 'read':line[2]}
#      for line in lines
#  ]
# return books

# def _save_all_books(books):
#    with open(books_file, 'w') as file:
#        json.dump(books,file)

#       for book in books:
#            file.write(f"{book['title']}, {book['author']}, {book['read']}\n")


def mark_book_as_read(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE title=?', (title,))


def delete_book(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE title=?', (title,))

    # books = get_all_books()
    # books = [book for book in books if book['title'] != title]
    # _save_all_books(books)

    # global books
    # books = [book for book in books if book['title'] != title]

    #
    # for book in books:
    #    if book['title'] == title:
    #        books.remove(book)
