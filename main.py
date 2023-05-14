import ruloc as ru
import effects as e
from random import randint

# Resources and modifiers
money = 100
military = 100
diplo = 100
happiness = 100
victory = False
c = 1


def txt(x):
    txt_sp = [0, ru.txteve1, ru.txteve2, ru.txteve3, ru.txteve4, ru.txteve5, ru.txteve6]
    print(txt_sp[x])


"""
Prints event flavor text and choices.
x - event identifier
"""

def random_event():
    global military, diplo, money, happiness
    random_txt_sp = [ru.rand_ev1, ru.rand_ev2, ru.rand_ev3, ru.rand_ev4, ru.rand_ev5, ru.rand_ev6,
                      ru.rand_ev7, ru.rand_ev8]
    x = randint(0, 7)
    print(random_txt_sp[x])
    ans = int(input())
    e.random_effct(x, ans)

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

while not victory and min(money, diplo, happiness, military) > 0:
    random_event()
    #event(c)
    c += 1


if victory:
    print("good")
else:
    print("bad")