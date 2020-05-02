

with open('poem.txt', 'r', encoding='utf-8') as file:
    first_letters = ''
    for i in file:
        first_letters += i[0]

    print(first_letters)
