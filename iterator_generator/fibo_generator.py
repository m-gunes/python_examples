def fibonacci():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        # a,b = b, a+b
        c = a+b
        a = b
        b = c
        yield b


max_value = 10

for i in fibonacci():
    if i > max_value:
        break
    print(i)


###########

def fibo(limit):
    a,b = 0,1
    while a < limit:
        yield a
        c = a + b
        b = a
        a = c
        # a, b = b, a + b


for i in fibo(5):
    print(i)












