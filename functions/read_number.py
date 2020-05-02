# kullanicidan iki basamakli sayi al ve bunun okunusunu bul

birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def find_number_read(num):
    first = num % 10
    second = num // 10
    return onlar[second] + ' ' + birler[first]


print(find_number_read(10))
