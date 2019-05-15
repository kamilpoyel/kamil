
f= open('plik.txt','r')


for line in f.readlines():
    print(line.strip())