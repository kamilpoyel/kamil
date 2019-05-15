import os

lista = os.listdir('bvb')

for item in lista:
    if os.path.isdir(item):
        print('{} jest folderem'.format(item))
    else:
        print('{} nie jest plikiem'.format(item))



