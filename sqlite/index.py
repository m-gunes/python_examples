import sqlite3
import time

class Book:
    def __init__(self, name, writer, publisher, type, publish):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.type = type
        self.publish = publish

    def __str__(self):
        return 'kitap ismi: {} /n yazar ismi: {} /n yayinci: {} /n tipi: {} /n, yayin: {} /n'.format(
            self.name, self.writer, self.publisher, self.type, self.publish
        )


class Bookshelf:
    def __init__(self):
        self.create_connect()

    def create_connect(self):
        self.connect = sqlite3.connect('bookshelf.db')
        self.cursor = self.connect.cursor()

        query = 'CREATE TABLE IF NOT EXISTS books (name TEXT, writer TEXT, publisher TEXT, type TEXT, publish INT)'
        self.cursor.execute(query)
        self.connect.commit()

    def close_connect(self):
        self.connect.close()

    def fetch_all(self):
        query = 'SELECT * FROM books'
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        if len(books) == 0:
            print('not found')
        else:
            for i in books:
                name, writer, publisher, type, publish = i
                book = Book(name, writer, publisher, type, publish)
                print(book) # tam burda Book class'inda tanimladigimiz __str__ calisacak

    def find_book(self, name):
        query = 'SELECT * FROM books WHERE name = ?'
        self.cursor.execute(query, (name,))
        books = self.cursor.fetchall()

        if len(books) == 0:
            print('not found')
        else:
            for i in books:
                name, writer, publisher, type, publish = i
                book = Book(name, writer, publisher, type, publish)
                print(book) # tam burda Book class'inda tanimladigimiz __str__ calisacak

    def add_book(self, book):
        name, writer, publisher, type, publish = book
        query = 'INSERT INTO books VALUES(?,?,?,?,?)'
        self.cursor.execute(query, (name, writer, publisher, type, publish))
        self.connect.commit()

    def remove_book(self, name):
        query = 'DELETE FROM books WHERE name = ?'
        self.cursor.execute(query, (name,))
        self.connect.commit()

    def increase_publish(self, name):
        query = 'SELECT * FROM books WHERE nama = ?'
        self.cursor.execute(query, (name,))
        books = self.cursor.fetchall()

        if len(books) == 0:
            print('not found')
        else:
            publish = books[0][4]
            publish += 1
            query2 = 'UPDATE books SET publish = ? WHERE name = ?'
            self.cursor.execute(query2, (publish, name))
            self.connect.commit()



