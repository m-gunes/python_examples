# ekok bulma

def ekok(a, b):
    num = 2
    ekok = 1

    while a != 1 or b != 1:
        if a % num == 0 and b % num == 0:
            a = a // num
            b = b // num
            ekok *= num
        elif a % num != 0 and b % num == 0:
            b = b // num
            ekok *= num
        elif a % num == 0 and b % num != 0:
            a = a // num
            ekok *= num
        else:
            num += 1

    return ekok


num1 = int(input('sayi giriniz'))
num2 = int(input('sayi giriniz'))
print(ekok(num1, num2))
