
class kalku():
    def __init__(self):
        print('int')
    def __int__(self):
        print('def')
    def dodaj(self,a,b):
        wynik= a+b
        print(wynik)
    def odejmij(self,a,b):
        wynik=a-b
        print(wynik)

def mian():
    print('1')
cal= kalku()

cal.dodaj(10,15)
cal.odejmij(10,15)


kal=kalku()
kal.dodaj(12,23)