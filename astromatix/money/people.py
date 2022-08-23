from os import*
def cls():
    system('cls')
c = input('')
cls()
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
def add(val):
    if input('') == '  ':
        cls()
        print(input('nna') + ' = ' + 'Empl(' + c + input('na') + c + ', ' + c + input('ra') + c + ', ' + c + input('jo') + c + ')')

lor = Empl('lorenzgage', 'Co. Founder', 'Driver')
kra = Empl('krayqwert', 'Founder', 'Manager')
while True:
    add('')