import os
from datetime import datetime

# print(*dir(os), sep='\n')

#  -get directory url
# print(os.getcwd())

# - change directory
# os.chdir('/Users/mgunes/Documents/experimental/ex_code/')

# - get item of directory
# print(os.listdir())
# for i in os.listdir():
#     print(i)

# - create dir
# os.mkdir('deneme')

# - create nested dir
# os.makedirs('deneme2/deneme3')

# - remove dir
# os.rmdir('deneme2/deneme3')
# os.rmdir('deneme')

# created again
# os.mkdir('deneme2/deneme3')

# - remove nested dir. remove sub dir. all
# os.removedirs('deneme2/deneme3')

# - rename file
# os.rename('test.txt', 'test2.txt')

# - get info of file
# print(os.stat('test2.txt'))
# print(datetime.fromtimestamp(os.stat('test2.txt').st_mtime))

# give us all file in dir. os.walk() is return generator

for dir, dir_name, file_name   in os.walk('/Users/mgunes/Documents/experimental/ex_code/'):
    # print('dir', dir)
    # print('dir name', dir_name)
    # print('file name', file_name)
    # print('**********')
    for i in file_name:
        if i.endswith('.py'):
            print(i)

