


while True:

    n = input('(exit q)bir sayi girniz:');
    if n == 'q':
        break;

    n = int(n)
    x = n - 1
    sum = 0

    while (x):
        if n % x == 0:
            sum += x
        x -= 1

    if sum == n:
        print('girdiginiz sayi mikemmel (sum)', sum)
    else:
        print('girdiginiz sayi mikemmel degil')
