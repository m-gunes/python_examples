def super_number(func):
    def wrapper(args):

        superNum = []
        for i in args:
            total = 0
            for j in range(1, i):
                if i % j == 0:
                    total += j
            if i == total:
                superNum.append(i)

        print('super numberes :', superNum)

        func(args)

    return wrapper


def is_prime_number(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


@super_number
def prime_number(numlist):
    prime = []
    for item in numlist:
        b = 2
        s = 0
        while b < item:
            if item % b == 0:
                s += 1
            b += 1
        if s == 0:
            prime.append(item)

        # if is_prime_number(i):
        #     prime.append(i)
    print('asal sayilar:', prime)
    return prime


prime_number(range(2, 1001))

# def avarage(liste):
#     total = 0
#     for i in liste:
#         total += i
#
#     return total / len(liste)
#
# print(avarage(range(100)))
