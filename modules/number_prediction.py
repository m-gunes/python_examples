# from random import randint
# from time import sleep
#
# random_number = randint(1,100)
# estimate_count = 7
#
# while True:
#
#     guess = int(input('tahmininiz: '))
#
#     estimate_count
#
#     if guess < random_number:
#         print('sorgulaniyor')
#         sleep(1) # 1 sn ye program durur
#         print('daha buyuk bir sayi giriniz')
#         estimate_count -= 1
#     elif guess > random_number:
#         print('sorgulaniyor')
#         sleep(1)  # 1 sn ye program durur
#         print('daha kucuk bir sayi giriniz')
#     else:
#         print('sorgulaniyor')
#         sleep(1)  # 1 sn ye program durur
#         print('Tebrikler')
#         break
#
#     if estimate_count == 0:
#         print('tahmin hakkiniz bitti')
#         break
#
#
#

from random import randint

small_number = 1
big_number = 100
random_number = randint(small_number, big_number)

while True:

    guess = int(input('tahmininiz: '))

    if guess < random_number:
        if small_number > guess:
            print("hani {}'dan buyuk sayi gicektin".format(small_number))
        else:
            small_number = guess
            print(str(guess) + '\'dan daha buyuk bir sayi giriniz')
    elif guess > random_number:
        if big_number < guess:
            print("hani {}'dan kucuk sayi gicektin".format(big_number))
        else:
            big_number = guess
            print(str(guess) + '\'dan daha kucuk bir sayi giriniz')
    else:
        print('boomm  kaybettiniz')
        break




