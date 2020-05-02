import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect('library.db') # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS bookshelf(name TEXT, author TEXT, publisher TEXT, page_count INT)')
    con.commit()

def insert_data():
    cursor.execute('INSERT INTO bookshelf VALUES("Istanbul Hatirasi", "Ahmet Umit", "Everest", 561)')
    con.commit()

def insert_data_input(name, author, publisher, page):
    cursor.execute('INSERT INTO bookshelf VALUES(?,?,?,?)', (name, author, publisher, page))
    con.commit() # veri tabaninda bir guncelleme yaparken

def fetch_all():
    cursor.execute('SELECT * FROM bookshelf')
    all_list = cursor.fetchall()  # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    for i in all_list:
        print(i)


def fetch_some():
    cursor.execute('SELECT name,author FROM bookshelf')
    all_list = cursor.fetchall()  # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    for i in all_list:
        print(i)

def filtered_fetch(publisher):
    cursor.execute('SELECT * FROM bookshelf WHERE publisher=?',(publisher,))
    filtered_list = cursor.fetchall()
    print(filtered_list)

def update_publisher(old, new):
    cursor.execute('UPDATE bookshelf SET publisher=? WHERE publisher = ?', (new, old))
    con.commit() # guncellemek istedigimizde

def remove_author(name):
    cursor.execute('DELETE FROM bookshelf WHERE author = ?',(name,))
    con.commit()


# fetch_all()
# fetch_some()
# filtered_fetch('Everest')
# update_publisher('sis', 'Everest')
remove_author('Ahmet Umit')

# name = input('kitap ismi')
# author = input('yazar ismi')
# publisher = input("yayin evi")
# page = int(input('sayfa sayisi'))
#
# insert_data_input(name, author, publisher, page)

con.close() # Bağlantıyı koparıyoruz.