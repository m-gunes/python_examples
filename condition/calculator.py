print(
    '''
    1. toplama islemi
    2. cikarma islemi
    3. carpma islemi
    4. bolme islemi
    
    '''
)

a = int(input('birinci sayi'))
b = int(input('ikinci sayi'))
islem = int(input('islem giriniz'))

if islem == 1:
    print('{} ile {} in toplami {} dir'.format(a, b, a + b))
elif islem == 2:
    print('{} ile {} in farki {} dir'.format(a, b, a - b))
elif islem == 3:
    print('{} ile {} in carpimi {} dir'.format(a, b, a * b))
elif islem == 4:
    print('{} ile {} in bolumu {} dir'.format(a, b, a / b))
else:
    print('gecersiz islem')
