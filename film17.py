try:
    plik=open('kz.txt','r+')
    plik.write('sima')
    plik.close()
except FileNotFoundError as e:
    print('wystapil blad')
    print(e)
except:
    print('nieznany blad')
