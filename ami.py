from time import*
from os import*
def down(num1, num2):
    return (num2 - num1)

def anim(val):
    for x in range(12):
        if x == (val + down(2, 10)):
            print('00000  00000')
        elif x == (val + down(1, 10)):
            print('00 00  00 00')
        elif x == (val + down(3, 10)):
            print('0000 00 0000')

        else:   
            print('000000000000')
    sleep(0.33)
    system('cls')
while True:
    anim(0)
    anim(1)
    anim(2)
    anim(1)
