from os import*
from random import*
score = 0
zton = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
screanxlan = 10
screanylan = 10
screan = {
    '00': '0',
    '10': '0',
    '20': '0',
    '30': '0',
    '40': '0',
    '50': '0',
    '60': '0',
    '70': '0',
    '80': '0',
    '90': '0',
    '01': '0',
    '11': '0',
    '21': '0',
    '31': '0',
    '41': '0',
    '51': '0',
    '61': '0',
    '71': '0',
    '81': '0',
    '91': '0',
    '02': '0',
    '12': '0',
    '22': '0',
    '32': '0',
    '42': '0',
    '52': '0',
    '62': '0',
    '72': '0',
    '82': '0',
    '92': '0',
    '03': '0',
    '13': '0',
    '23': '0',
    '33': '0',
    '43': '0',
    '53': '0',
    '63': '0',
    '73': '0',
    '83': '0',
    '93': '0',
    '04': '0',
    '14': '0',
    '24': '0',
    '34': '0',
    '44': '0',
    '54': '0',
    '64': '0',
    '74': '0',
    '84': '0',
    '94': '0',
    '05': '0',
    '15': '0',
    '25': '0',
    '35': '0',
    '45': '0',
    '55': '0',
    '65': '0',
    '75': '0',
    '85': '0',
    '95': '0',
    '06': '0',
    '16': '0',
    '26': '0',
    '36': '0',
    '46': '0',
    '56': '0',
    '66': '0',
    '76': '0',
    '86': '0',
    '96': '0',
    '07': '0',
    '17': '0',
    '27': '0',
    '37': '0',
    '47': '0',
    '57': '0',
    '67': '0',
    '77': '0',
    '87': '0',
    '97': '0',
    '08': '0',
    '18': '0',
    '28': '0',
    '38': '0',
    '48': '0',
    '58': '0',
    '68': '0',
    '78': '0',
    '88': '0',
    '98': '0',
    '09': '0',
    '19': '0',
    '29': '0',
    '39': '0',
    '49': '0',
    '59': '0',
    '69': '0',
    '79': '0',
    '89': '0',
    '99': '0'
}
class sprite:
    def __init__(spr, x, y):
        spr.x = x
        spr.y = y
    def move(spr):
        inpu = input('')
        if inpu == 'w':
            if spr1.y != 0:
                screan[str(spr1.x) + str(spr1.y)] = '0'
                spr1.y -= 1
                screan[str(spr1.x) + str(spr1.y)] = '1'
        elif inpu == 's':
            if spr1.y != 9:
                screan[str(spr1.x) + str(spr1.y)] = '0'
                spr1.y += 1
                screan[str(spr1.x) + str(spr1.y)] = '1'
        elif inpu == 'd':
            if spr1.x != 9:
                screan[str(spr1.x) + str(spr1.y)] = '0'
                spr1.x += 1
                screan[str(spr1.x) + str(spr1.y)] = '1'
        elif inpu == 'a':
            if spr1.x != 0:
                screan[str(spr1.x) + str(spr1.y)] = '0'
                spr1.x -= 1
                screan[str(spr1.x) + str(spr1.y)] = '1'
        return scrprint()
spr1 = sprite(0, 0)
enemy = sprite(9, 9)
screan[str(enemy.x) + str(enemy.y)] = '2'
def scrprint():
    screan[str(spr1.x) + str(spr1.y)] = '1'
    for x in range(screanxlan * screanylan):
        if x < 10:
            screan[str(x) + '0']
        else:
            screan[str(x)]
    system('cls')
    screan[str(spr1.x) + str(spr1.y)] = '1'
    keyline = ''
    for x in range(int((len(screan)) / (screanxlan))):
        screan[str(spr1.x) + str(spr1.y)] = '1'
        for y in range(screanylan):
            keyline += screan[str(y) + str(x)] + '   '
        print(keyline)
        keyline = ''
        screan[str(spr1.x) + str(spr1.y)] = '1'
    print('score: ' + str(score))
    print('high score: 301')
scrprint()
while True:
    if str(spr1.x) + str(spr1.y) == str(enemy.x) + str(enemy.y):
        enemy = sprite(choice(zton), choice(zton))
        score += 1
    screan[str(enemy.x) + str(enemy.y)] = '2'
    scrprint()
    spr1.move()