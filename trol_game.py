from random import randint
otvet = randint(1,100)
user_input = int(input('попробуй угадать число от одного до ста:'))
game = True
while game:
    if user_input == otvet:
        print('хорош')
        break
    else:
        if otvet > user_input:
            user_input = int(input(f'неправильно. попробуй ввести число меньше {user_input}'))
        elif otvet < user_input:
            user_input = int(input(f'неправильно.попробуй написать число больше {user_input}'))
    
