import ruloc as ru

money = 100
military = 100
diplo = 100
happiness = 100

def effct(x, y):
    if x == 3:
        if y == 1:
            print(ru.result1)


def random_effct(x, y):
    global military, diplo, money, happiness
    if x == 1:
        if y == 1:
            military -= 15
        elif y == 2:
            diplo += 10
            money -= 15
        else:
            happiness -= 20
    elif x == 2:
        if y == 1:
            military -= 15
            happiness -= 20
        else:
            money -= 20
            happiness += 20
    elif x == 3:
        happiness -= 10
        money -= 15
    elif x == 4:
        money += 20
    elif x == 5:
        money -= 10
    elif x == 6:
        military -= 20
    elif x == 7:
        if y == 1:
            happiness += 20
        elif y == 2:
            money -= 30
            happiness += 30
            diplo -= 10
        else:
            happiness -= 10
    elif x == 8:
        if y == 1:
            money -= 10
            happiness += 15
        else:
            happiness -= 15
    print(ru.money, money)
    print(ru.military, military)
    print(ru.happiness, happiness)
    print(ru.diplo, diplo)



"""
Changes player resources and modifiers according to player's choices.
x - event identifier 
y - choice identifier
"""