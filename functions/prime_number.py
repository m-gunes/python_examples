# def is_prime_number(number):
#     number = int(number)
#     index = number - 1
#     if number <= 1:
#         return False
#
#     while(index > 1):
#         if number % index == 0:
#             return False
#         index -= 1
#
#     return True

# another way to make

def is_prime_number(number):
    number = int(number)
    if number <= 1:
        return False
    elif number == 2:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


while True:
    num = input('sayi giriniz:')
    if num == 'q':
        break

    if is_prime_number(num):
        print(num, 'asal sayi')
    else:
        print(num, 'asal sayi degil')


# another good way to apply
#
# def isPrimeNumber(x):
#     i = 2
#     if x <= 1:
#         return False
#     elif x == 2:
#         return True
#     else:
#         while i < x:
#             if x % i == 0:
#                 return False
#             i+=1
#     return True
