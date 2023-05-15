import ruloc as ru
import effects as e
from random import randint
# Salaries
'''
Yaroslav Elizarev = 40
Alexey Polevik =
Egor Nechaev =
'''


# Resources and modifiers
money = 100
military = 100
diplo = 100
happiness = 100
victory = False
c = 1


def txt(x):
    txt_sp = [0, ru.txteve1, ru.txteve2, ru.txteve3, ru.txteve4, ru.txteve5, ru.txteve6, ru.texteve7, ru.txteve8,
              ru.txteve9, ru.txteve10, ru.txteve11, ru.txteve12, ru.txteve13, ru.txteve14]
    print(txt_sp[x])


"""
Prints event flavor text and choices.
x - event identifier
"""

def random_event():
    global military, diplo, money, happiness
    random_txt_sp = [ru.rand_ev1, ru.rand_ev2, ru.rand_ev3, ru.rand_ev4, ru.rand_ev5, ru.rand_ev6,
                      ru.rand_ev7, ru.rand_ev8]
    x = randint(1, 8)
    print(random_txt_sp[x])
    ans = int(input())
    e.random_effct(x, ans)

'''
Prints random event flavor text and choices.
'''
def event(x):
    txt(x)
    ans = int(input())
    e.effct(x, ans)


"""
Event function. Calls txt function and effct function.
x - event identifier
"""
print(ru.start_text)
print(ru.exposition_text)
a = input()
while not victory and min(money, diplo, happiness, military) > 0:
    if c > 2 and c % 2 == 1:
        random_event()
    event(c)
    c += 1


if victory:
    print(ru.good_end)
else:
    print(ru.bad_end)