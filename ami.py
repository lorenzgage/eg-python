from time import*
from os import*
num = 0
while True:    
    for x in range(5):
        if x == (num + 2):
            print('00000  00000')
        elif x == (num + 1):
            print('00 00  00 00')
        elif x == (num + 3):
            print('0000 00 0000')

        else:   
            print('000000000000')
    sleep(0.25)
    system('cls')
    num += 1    
    for x in range(5):
        if x == (num + 2):
            print('00000  00000')
        elif x == (num + 1):
            print('00 00  00 00')
        elif x == (num + 3):
            print('0000 00 0000')

        else:   
            print('000000000000')
    sleep(0.25)
    system('cls')
    num -= 1
    for x in range(5):
        if x == (num + 2):
            print('00000  00000')
        elif x == (num + 1):
            print('00 00  00 00')
        elif x == (num + 3):
            print('0000 00 0000')

        else:   
            print('000000000000')
    sleep(0.25)
    system('cls')
    num -= 1    
    for x in range(5):
        if x == (num + 2):
            print('00000  00000')
        elif x == (num + 1):
            print('00 00  00 00')
        elif x == (num + 3):
            print('0000 00 0000')

        else:   
            print('000000000000')
    sleep(0.25)
    system('cls')
    num += 1   
