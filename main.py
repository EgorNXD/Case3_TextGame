import ruloc as ru
import effects as e


def txt(x):
    txteve1 = ru.txteve1
    txteve2 = ru.txteve2
    txteve3 = ru.txteve3
    txt_sp = [0, txteve1, txteve2, txteve3]
    print(txt_sp[x])


"""
Prints event flavor text and choices.
x - event identifier
"""


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
#resorces and indicators
event(1)
res1 = 100
res2 = 100
res3 = 100
victory = False
indicator = 100
c = 1

while victory is False and indicator > 0:
    print('', res1)
    print('', res2)
    print('', res3)
    print('', indicator)
    random_event(c)
    event(c)
    c += 1

