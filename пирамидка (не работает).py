user_input = int(input('введите число'))
def piramidka(user_input):
    i = 1
    piram = []
    while i == user_input:
             k = i * '*'
             piram += k
             i+= 1
    return piram
print(piramidka(user_input))
