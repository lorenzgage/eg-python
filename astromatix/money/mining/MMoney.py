from os import*
from math import*
import random
from time import sleep
system('cls')
def ERROR(type, val):
    print(str(type) + ' error: ' + val)
def clear():
    system('cls')
def bar(pri):
    clear()
    aran = [0.25, 0.50, 0.75, 1]
    ran = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
    stri = ''
    num = -1
    while (num <= 10):
        stri = ''
        system('cls')
        for x in ran:
            stri += str(x)
            num += 1
            ran[num] = '■'
            if (pri != 0):
                print(pri)
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

dots = ['.', '..', '...']
numb = 0

def calc(*lan):
    numb = 0
    system('cls')
    if (lan[1] != None):
        print(lan[1])
    for x in range(int(lan[0])):
        print('calculating' + dots[numb])
        sleep(0.50)
        system('cls')
        numb += 1
        if numb > 2:
            numb = 0
        if (lan[1] != None):
            print(lan[1])

def amountEntry():
    amount = int(input('Miners '))
    if amount <= 0:
        system('cls')
        ERROR('parse', 'Miners')
        return amountEntry()
    calc(4, None)
    return amount

def moneyEntry():
    system('cls')
    money = int(input('Money Made '))
    if money <= 0:
        system('cls')
        ERROR('parse', 'Money Made')
        return moneyEntry()
    if (money > 5000):
        money -= 5000
    calc(3, None)
    return money

amount = amountEntry()
money = moneyEntry()

system('cls')
FM = ((int(money) / 1.75) / int(amount))
print(str(FM))
sleep(0.75)
calc(3, str(FM))
print(str(int(money) - (int(amount) * int(FM))))