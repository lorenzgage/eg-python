from time import*
times = {
    "Time": 'Clocking'
}
clo = 0
vel = False
while vel:
        clo += 1
        sleep(1)
while True:
    clo = 0
    for x in range(1):
        name = input('name')
        vel = True
        sleep(1)
        vel = False
    times.update({name: clo})
    for x, y in times.items():
        print(x, y)
