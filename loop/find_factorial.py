# n * n-1

print('''

faktoriel hesaplama

exit q

''')

while True:
    n = input('sayi giriniz?: ')

    if n == 'q':
        break

    n = int(n)
    fac = 1
    while n:
        fac *= n
        n -= 1

    print(fac)


# another way to make
#
# while True:
#
#     n = input('sayi giriniz?: ')
#
#     if n == 'q':
#         break
#
#     n = int(n)
#     fac = 1
#
#     for i in range(2, n+1):
#         fac *= i
#
#
#     print(fac)


# def factorial(number):
#     fac = 1
#     if number == 1 or number == 0:
#         return print(fac)
#
#     while (number > 1):
#         fac *= number
#         number -= 1
#     print(fac)

