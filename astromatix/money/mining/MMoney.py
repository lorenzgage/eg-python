from os import*
from math import*
import random
from time import sleep
system('cls')
class Per:
    def __init__(self, name):
        self.name = name

class Empl(Per):
    def __init__(self, name, rank, job):
        super().__init__(name)
        self.rank = rank
        self.job = job
    def una(self):
        return self.name
    def ura(self):
        return self.rank
    def ujo(self):
        return self.job
    def use(name):
        return name.__module__

lorenzgage = Empl('lorenzgage', 'Co. Founder', 'Driver')
krayqwert = Empl('krayqwert', 'Founder', 'Manager')
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

def driverEntry():
    driver = (input('driver '))
    calc(4, None)
    return driver

amount = amountEntry()
money = moneyEntry()
driver = driverEntry()

if driver == Empl.__name__:
    driver.use
    if driver.job == 'Driver':
        print('good')
else:
    print(str(driver))

system('cls')
FM = ((int(money) / 1.75) / int(amount))
print(str(FM))
sleep(0.75)
calc(3, str(FM))
print(str(int(money) - (int(amount) * int(FM))))