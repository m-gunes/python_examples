
# bir sayinin tam bolenlerini bulma

def full_divisor(num):
    arr = []
    for i in range(2, num):
        if num % i == 0:
            arr.append(i)

    return arr

while True:
    num = input('sayi giriniz:')
    if num == 'q':
        break
    else:
        print('tam bolenler listesi', full_divisor(int(num)))
