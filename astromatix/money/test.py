from os import*
from random import*
score = 0
HScore = 5
game_on = True
wwep = False
num3 = 1
num = 0
onetwo = 0
zton = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
screanxlan = 10
screanylan = 10
screan = {'00': '0', '01': '0', '02': '0', '03': '0', '04': '0', '05': '0', '06': '0', '07': '0', '08': '0', '09': '0', '10': '0', '11': '0', '12': '0', '13': '0', '14': '0', '15': '0', '16': '0', '17': '0', '18': '0', '19': '0', '20': '0', '21': '0', '22': '0', '23': '0', '24': '0', '25': '0', '26': '0', '27': '0', '28': '0', '29': '0', '30': '0', '31': '0', '32': '0', '33': '0', '34': '0', '35': '0', '36': '0', '37': '0', '38': '0', '39': '0', '40': '0', '41': '0', '42': '0', '43': '0', '44': '0', '45': '0', '46': '0', '47': '0', '48': '0', '49': '0', '50': '0', '51': '0', '52': '0', '53': '0', '54': '0', '55': '0', '56': '0', '57': '0', '58': '0', '59': '0', '60': '0', '61': '0', '62': '0', '63': '0', '64': '0', '65': '0', '66': '0', '67': '0', '68': '0', '69': '0', '70': '0', '71': '0', '72': '0', '73': '0', '74': '0', '75': '0', '76': '0', '77': '0', '78': '0', '79': '0', '80': '0', '81': '0', '82': '0', '83': '0', '84': '0', '85': '0', '86': '0', '87': '0', '88': '0', '89': '0', '90': '0', '91': '0', '92': '0', '93': '0', '94': '0', '95': '0', '96': '0', '97': '0', '98': '0', '99': '0'}
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
    def track(gorilla1):
        screan[str(gorilla.x) + str(gorilla.y)] = '0'
        if wwep == True:
            if gorilla.x > spr1.x:
                gorilla.x += 1
            elif gorilla.x < spr1.x:
                gorilla.x -= 1
            if gorilla.y > spr1.y:
                gorilla.y += 1
            elif gorilla.y < spr1.y:
                gorilla.y -= 1
        else:
            if gorilla.x < spr1.x:
                gorilla.x += 1
            elif gorilla.x > spr1.x:
                gorilla.x -= 1
            if gorilla.y < spr1.y:
                gorilla.y += 1
            elif gorilla.y > spr1.y:
                gorilla.y -= 1
        screan[str(gorilla.x) + str(gorilla.y)] = '3'
        
spr1 = sprite(0, 0)
enemy = sprite(9, 9)
gorilla = sprite(0, 9)
wep = sprite(9, 0)
screan[str(enemy.x) + str(enemy.y)] = '2'
screan[str(gorilla.x) + str(gorilla.y)] = '3'
def scrprint():
    for x in range(screanxlan * screanylan):
        if x < 10:
            screan[str(x) + '0']
        else:
            screan[str(x)]
    system('cls')
    keyline = ''
    for x in range(int((len(screan)) / (screanxlan))):
        for y in range(screanylan):
            keyline += screan[str(y) + str(x)] + ' '
        print(keyline)
        keyline = ''
    print('score: ' + str(score))
    print('high score: ' + str(HScore))
scrprint()
while True:
    onetwo += 1
    if onetwo == 3:
        if wwep == False:
            gorilla.track()
            if str(spr1.x) + str(spr1.y) == str(gorilla.x) + str(gorilla.y):
                game_on = False
                system('cls')
            else:
                if str(spr1.x) + str(spr1.y) == str(gorilla.x) + str(gorilla.y):
                    game_on = 'win'
                    system('cls')
            onetwo = 0
    system('cls')
    if game_on == True:
        if score > 1:
            screan[str(wep.x) + str(wep.y)] = '7'
            if str(spr1.x) + str(spr1.y) == str(wep.x) + str(wep.y):
                wwep = True
                screan[str(spr1.x) + str(spr1.y)] = '4'
        if str(spr1.x) + str(spr1.y) == str(enemy.x) + str(enemy.y):
            enemy = sprite(choice(zton), choice(zton))
            score += 1
            if score > HScore:
                HScore += 1
        screan[str(enemy.x) + str(enemy.y)] = '2'
        screan[str(gorilla.x) + str(gorilla.y)] = '3'
    elif game_on == 'win':
        print('You Win')
    else:
        print(str(game_on))
    if wwep == True:
        screan[str(spr1.x) + str(spr1.y)] = '4'
        screan[str(wep.x) + str(wep.y)] = '0'
    else:
        scrprint()
        spr1.move()
