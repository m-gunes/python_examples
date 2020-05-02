
m , g = 'mustafa', 'gunes'
print(m,g)

a = 1
b = 1

fibo = [a, b]

for i in range(10):
    a, b = b, a + b
    # c = a + b
    # a = b
    # b = c
    fibo.append(b)

print(fibo)
