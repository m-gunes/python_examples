def is_perfect(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += i

    return count == num


for i in range(1, 1000):
    if is_perfect(i):
        print(i, 'mikemmel')
