# ebob bulma

def ebob(a, b):
    num = 2
    ebob = 1

    while a != 1 or b != 1:
        if a % num == 0 and b % num == 0:
            a //= num
            b //= num
            ebob *= num
        elif a % num != 0 and b % num == 0:
            b //= num
        elif a % num == 0 and b % num != 0:
            a //= num
        else:
            num += 1

    return ebob


print(ebob(15, 100))

# another way to make
# def ebob_bulma(sayı1, sayı2):
#     i = 1
#     ebob = 1
#     while (i <= sayı1 and i <= sayı2):
#
#         if (not (sayı1 % i) and not (sayı2 % i)):
#             ebob = i
#         i += 1
#     return ebob
#
#
# print("Ebob:", ebob_bulma(24, 32))
