from math import*
import random
from time import*
from os import*
def clear():
    system('cls')
clear()
def bar():
    clear()
    aran = [0.25, 0.50, 0.75, 1, 1.25, 1.50]
    ran = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
    stri = ''
    num = -1
    while (num <= 10):
        stri = ''
        clear()
        for x in ran:
            stri += str(x)
            num += 1
            ran[num] = '■'
            print(stri)
            sleep(random.choice(aran))
        if (num == 25):
            num += 1
            clear()
            sleep(0.50)
            print(stri)
            sleep(0.25)
            clear()
            print(stri)
bar()