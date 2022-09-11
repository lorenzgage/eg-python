from os import*
def cls():
    system('cls')
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
    def use(name):
        return name.__module__
def add(val):
    if input('') != None:
        cls()
        print(input('nna') + ' = ' + 'Empl(\'' + input('na') + '\', \'' + input('ra') + '\', \'' + input('jo') + '\')')

lor = Empl('lorenzgage', 'Co. Founder', 'Driver')
kra = Empl('krayqwert', 'Founder', 'Manager')
while True:
    add('')
