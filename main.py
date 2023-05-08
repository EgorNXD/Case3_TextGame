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

event(1)
