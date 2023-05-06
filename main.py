import ruloc as ru
import effects as e

def event(X):
    ru.loc(X)
    ans = int(input())
    if ans == 1:
        e.eff(X, 1)
    if ans == 2:
        e.eff(X, 2)
    if ans == 3:
        e.eff(X, 3)


event(1)