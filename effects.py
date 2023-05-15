import ruloc as ru

money = 100
military = 100
diplo = 100
happiness = 100

def effct(x, y):
    global military, diplo, money, happiness, victory
    if x == 1:
        if y == 1:
            happiness -= 10
            military += 100
        elif y == 2:
            money -= 10
            military += 100
        else:
            diplo -= 30
            military += 150
    elif x == 2:
        if y == 1:
            military -= 30
            diplo -= 10
        elif y == 2:
            military -= 50
        else:
            military -= 80
            diplo += 20
    elif x == 3:
        if y == 1:
            diplo += 10
            happiness += 20
            print(ru.result1)
        elif y == 2:
            military -= 20
            happiness -= 10
    elif x == 4:
        if y == 1:
            money += 30
            happiness -= 10
        elif y == 2:
            money -= 50
            happiness += 10
    elif x == 5:
        if y == 1:
            print(ru.result2)
            diplo += 30
            happiness += 15
            money += 10
        else:
            military += 15
            happiness -= 10
    elif x == 6:
        if y == 1:
            print(ru.result3)
            happiness -= 10
            money -= 10
            diplo -= 10
        else:
            diplo += 10
            happiness += 20
    elif x == 7:
        if y == 1:
            happiness += 10
        else:
            happiness += 15
            money -= 10
    elif x == 8:
        if y == 2:
            print(ru.result4)
            military -= 20
            money -= 20
        else:
            diplo += 5
            happiness += 5
    elif x == 9:
        if y == 1:
            military -= 5
            diplo -= 5
        else:
            happiness -= 10
            money += 5
    elif x == 10:
        if y == 1:
            money += 10
        else:
            diplo -= 10
            happiness += 10
    elif x == 11:
        if y == 1:
            money *= 1.2
        elif y == 2:
            diplo *= 1.2
        else:
            happiness *= 1.2
    elif x == 12:
        if y == 1:
            military -= 10
            money += 15
            diplo += 10
        else:
            happiness += 20
    elif x == 13:
        if y == 1:
            diplo += 20
        else:
            money -= 10
            diplo += 30
    elif x == 14:
        if y == 1:
            money -= 40
        elif y == 2:
            diplo -= 40
        elif y == 3:
            military -= 40
        else:
            happiness -= 40
        victory = True
    print(ru.military, military)
    print(ru.happiness, happiness)
    print(ru.diplo, diplo)
    print(ru.money, money)






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