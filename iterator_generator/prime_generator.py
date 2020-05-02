
def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def prime_generator():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


for i in prime_generator():
    if i > 1000:
        break
    print(i)

