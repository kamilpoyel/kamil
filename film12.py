import time
print("start")
time.sleep(2)
print('stop')

timer = time.time()
time.sleep(2)
elepsed = time.time()-timer
print(elepsed)


timer = time.time()
timer2 = time.time()
while True:
    if time.time()-timer >2:
        print('ban')
        timer = time.time()

    if time.time()-timer2 >5:
        break

import datetime
teraz= datetime.datetime.now()
print(teraz)