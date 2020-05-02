from random import randint
from time import sleep

random_number = randint(1,100)
estimate_count = 7

while True:

    guess = int(input('tahmininiz: '))

    estimate_count

    if guess < random_number:
        print('sorgulaniyor')
        sleep(1) # 1 sn ye program durur
        print('daha buyuk bir sayi giriniz')
        estimate_count -= 1
    elif guess > random_number:
        print('sorgulaniyor')
        sleep(1)  # 1 sn ye program durur
        print('daha kucuk bir sayi giriniz')
    else:
        print('sorgulaniyor')
        sleep(1)  # 1 sn ye program durur
        print('Tebrikler')
        break

    if estimate_count == 0:
        print('tahmin hakkiniz bitti')
        break



