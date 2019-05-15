class kalku():
    def __init__(self):
       self.ostat_wyn=0

    def dodaj(self,a,b):
        wynik= a+b
        self.ostat_wyn=wynik
        print(wynik)
    def odejmij(self,a,b):
        wynik=a-b
        print(wynik)

calc= kalku()
calc.dodaj(5,3)
calc.dodaj(10,10)



calc2=kalku()
calc2.dodaj(50,50)
calc2.dodaj(510,350)
print("ostatni wynik{}".format(calc.ostat_wyn))
print("ostatni wynik{}".format(calc2.ostat_wyn))