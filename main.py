import ruloc as ru
import effects as e

def txt(X):
    txteve1 = ru.txteve1
    txteve2 = ru.txteve2
    txteve3 = ru.txteve3
    txt_sp = [0, txteve1, txteve2, txteve3]
    print(txt_sp[X])


def event(X):
    txt(X)
    ans = int(input())
    if ans == 1:
        e.eff(X, 1)
    if ans == 2:
        e.eff(X, 2)
    if ans == 3:
        e.eff(X, 3)


event(1)