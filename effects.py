import ruloc as ru


def effct(x, y):
    if x == 1:
        if y == 1:
            print(ru.result1_1)
        elif y == 2:
            print(ru.result1_2)
        else:
            print(ru.result1_3)


"""
Changes player resources and modifiers according to player's choices.
x - event identifier 
y - choice identifier
"""