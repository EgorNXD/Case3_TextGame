import ruloc as ru
import effects as e
from random import randint

def txt(x):
    txt_sp = [0, ru.txteve1, ru.txteve2, ru.txteve3, ru.txteve4, ru.txteve5, ru.txteve6]
    print(txt_sp[x])


"""
Prints event flavor text and choices.
x - event identifier
"""

def random_event(military, diplo, happiness, money):
    random_txt_sp = [ru.rand_ev1, ru.rand_ev2, ru.rand_ev3, ru.rand_ev4, ru.rand_ev5, ru.rand_ev6,
                      ru.rand_ev7, ru.rand_ev8]
    x = randint(0, 8)
    print(random_txt_sp[x])
    ans = int(input())
    e.random_effct(x, ans, military, diplo, happiness, money)

'''
Prints random event flavor text and choices.
'''
def event(x):
    txt(x)
    ans = int(input())
    if ans == 1:
        e.effct(x, 1)
    if ans == 2:
        e.effct(x, 2)
    if ans == 3:
        e.effct(x, 3)


"""
Event function. Calls txt function and effct function.
x - event identifier
"""



# Resources and modifiers
money = 100
military = 100
diplo = 100
happiness = 100
victory = False
c = 1

while not victory and min(money, diplo, happiness, military) > 0:
    print(ru.money, money)
    print(ru.military, military)
    print(ru.diplo, diplo)
    print(ru.happiness, happiness)
    random_event(military=military, diplo=diplo, happiness=happiness, money=money)
    event(c)
    c += 1


if victory:
    print("good")
else:
    print("bad")