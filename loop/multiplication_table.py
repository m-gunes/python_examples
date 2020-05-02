
for i in range(1, 11):
    for j in range(1, 11):
        print('{} x {} = {}'.format(i, j, i*j))

    print('\n')


# 1 den 100 e kadar 3 e bolunebilen sayilari continue kullanarak bastirmak
# for i in range(1, 101):
#     if i % 3 != 0:
#         continue
#     print(i)


# # list comprehension kullanarak 1'den 100'e cift sayilari bastirmak
# even = [i for i in range(1, 101) if i % 2 == 0]
# print(even)


