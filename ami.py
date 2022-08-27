from time import*
from os import*
def anim(val):
    for x in range(5):
        if x == (val + 2):
            print('00000  00000')
        elif x == (val + 1):
            print('00 00  00 00')
        elif x == (val + 3):
            print('0000 00 0000')

        else:   
            print('000000000000')
    sleep(0.33)
    system('cls')
while True:
    anim(0)
    anim(1)
