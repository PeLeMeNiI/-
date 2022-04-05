sm_al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
user_input = input('введи предложение: ')
sm_count = 0
bg_count = 0
def counter(user_input):
    for i in user_input:
        if i == sm_al:
            sm_count +=1
        elif i == big_al:
            bg_count +=1
    return (f'сдесь {sm_count} маленьких букв и {bg_count} заглавных')

print (counter(user_input))
