class Book:
    def __init__(self, name, author, type):
        print('init function')
        self.name = name
        self.author = author
        self.type = type

    def __str__(self):  # bu class'tan yaratilan obje printte yazilirsa asagidaki return ediyor
        return 'name: {} \nauthor: {} \ntype: {}'.format(self.name, self.author, self.type)

    def __del__(self):
        print('deleting.... the {} of {}'.format(self.name, self.author))


book1 = Book('kadinlar', 'Charler Bukowski', 'genel')

print(book1)

del book1

print(book1)
