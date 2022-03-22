def palindrom (x):
    if x == x[::-1]:
        return f'слово {x} палиндром'
    else:
        return f'слово {x} не палиндром'
