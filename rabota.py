#shopping_list = []
#while True:
#    user_input = input('что вы хотите добавить в список?')
#    if user_input.lower() == 'выход':
#      break
#    shopping_list.append(user_input)
#    print(f'вот что сейчас лежит в списке:{shopping_ list}')

#row = '*_*_'
#counter = 0
#for i in range(len(row)):
#   if row[i] == '*':
#     counter += 1
#print(counter)

#total_games = []
#while True:
#   user_input = input('какую игру вы хотите добавить в список?')
#   if user_input.lower() == ('выход'):
#      break
#   user_input_re = input('какой рейтинг будет у этой игры?')
#   if user_input_re.lower() == ('выход'):
#      break
#   else:
#       user_input_re.lower()
#       
#   pair = user_input, user_input_re
#   total_games.append(pair)
 #  print(f'вот какие игры есть в списке: {total_games}')
   
#while True:
#   print('купи слон, допрый чилавек')
#   if True:
#      user_input = input('введи ответ')
#      print(f'Фсе говорить {user_input},а ты купить слон')
#row = input('введите число')
#counter = 0
#for i in range(len(row)):
#   if row[i] == '1':
#     counter += 1
#print(counter)

#glasnie = ['а,е,ё,и,о,у,ы,э,ю,я']
#soglasnie = ['б,в,г,д,ж,з,й,к,л,м,н,п,р,с,т,ф,х,ц,ч,ш,щ']
#sogl = 0
#glasn = 0
#user_input = input('введите cлово')
#for i in range(len(user_input)):
   #if user_input[i] == soglasnie:
      #sogl += 1
#for d in range(len(user_input)):
  # if user_input[i] == glasnie:
 #     glasn += 1
 #  print(f'тут {sogl} и {glasn} гласных')

#user_input = int(input('ведите число'))
#x = 1
#deli = []
#while True:
#   for deli in range(1, user_input+1):
 #     if user_input % x == 0:
  #       x += 1
 ##        print (deli)
 #     else:
         #x += 1
#numbers = [7,4,5,10,7,14,22,4,2,3]
#tap_min = numbers[0]
#tap_max = numbers[0]
#for i in numbers:
   
   #if i > tap_max:
      #tap_max = i
   #if i < tap_min:
     # tap_min = i

#print(tap_min)
#print(tap_max)

#user_input = input() # привет
#glasn = ['а','е','ё','и','о','у','ы','э','ю','я']
#soglasn = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ']
#counter_s = 0
#counter_g = 0
#for i in range(len(user_input)):
#   current_letter = user_input[i]
#   for j in glasn:
 #     if current_letter == j:
 #        counter_g += 1
 # for a in soglasn:
  #    if current_letter == a:
#         counter_s += 1

#print(f'сдесь{counter_g} гласных и {counter_s} согласных.')


#user_input = int(input('введите число'))
#numbers = 0
#last = 0
#for i in range(1, user_input+1):
#   numbers+=i

#for a in range(numbers+1):
  # a*last
  # last+=a
   
#print(f'{numbers}')

#procent = int(input('Под какой процент вы кладете деньги:'))
#summ = int(input('Сколько вы хотите положить денег в банк?:'))
#years = int(input('а скольк лет вы хотите положить деньги в банк:'))
#num_of_year = 0
#money = 0
#for i in range(years):
  # money = (summ/100 * procent) + summ
   #summ = money
   #num_of_year +=1
   #print(f'год {num_of_year}. на вашем счету {money} р.')

#def is_even(n):

    #return n % 2 == 0
#print(is_even(3))

#def add_one(x):
#   print(f'добавь 1 к {x}')
#   x = x+1
#   return x

#x = 3

#z = add_one(x)
#foo = add_one(5)
#print(f'{z}, {foo}')

#def print_name(name):
 #  print(f'hello {name}')
 #  return

#print_name('khihiih')

#def last_element(e):
    #return e[-1]

#f = last_element([1,2,3,4,])
#s = last_element([5,6,7,8])
#print(f)
#print(s)

#name = 'unknown'
#lastname = 'unknownovich'

#def all_name(x, y):

   #return f'{x} {y}'

#print(all_name(name, lastname))

#def minus(x):
    #if x == 0:
     #  print('0')
   # elif x < 0:
     #  print(f'{x}')
 #   else:
#       print(f'-{x}')
 #   return(x)
#spisok = []
#def between(x,y):
   # for i in range(x,y+1):
    #   spisok.append(i)
    #return(spisok)

#def is_div(x,y,z):
  # if x%y==0 and x%z==0:
      # return True
 #  else:
      #return False
#dpisok = []
#def find_srar():
  #  if

  #  return spisok

#def repeat(x,y):
#   rep = x*y
#   return rep
#def find_smallest(numbers):
 #  last_num = numbers[0]
 #  for i in numbers:
  #    if i<last_num:
  #       last_num = i
#
 #  return last_num
      

#print(find_smallest([34,43,21,7]))

#def bool_to_words(x):
#  if x:
#   return ('Yes')
#  else:
#    return('no')


#x = []
#y = []
#def array_plus_array(x,y):
#   li = x+y
#   r = 0
#   for i in li:
#      r += i
#   return r

#def update_color(x):
#   if x == 'green':
#      return('yellow')
#   elif x == 'yellow':
#      return('red')
#   elif x == 'red':
#      return('green')

#def century_maker(x):
#   g = x // 100
#   if g % 100 == 0:
#       return g
  # else:
#      return g + 1

#def step_summ(x,y,z):
# r = 0
# for i in range(x,y+1,z):
#    r += i

 # return r
#x = []
#def word_filter(x):
#ban = [поставишь]
# for i in x[:]:
#     for j in ban:
#        if i == j:
#           x.remove(j)
# return x

#def generate_shape(x):
#   w = x * '+'
#    d = x * w
#    for smth in d:
                    #######
                   # =   = #
                  # |*| |*| #
                  #  -   -  #
                   #   ()  #

#import time
#def build_house(my_dream, colors):
'''   house = False
    roof_color = colors[0]
    house_color = colors[1]
    door_color = colors[2]
    roof = my_dream[0]
    walls = my_dream[1]
    
    while not house:
        roof_status = build_roof(roof,roof_color)
        walls_status = build_walls(walls,house_color)
        door_status = build_door(door_color,door_color)
        if roof_status == True and walls_status == True and door_status == True:
            house = True
            print('wonderful')
            www = print(f'{house}')
            time.sleep(2)
            print('wonderful')
                  
    return house
def build_roof(r,rc):
    return True
def build_walls(r,wc):
    return True
def build_door(r,dc):
    return True

idea = ('roof','walls')
colors = ('red','white','blue')
build_house(idea, colors)'''


'''savings = int(input('кольок денег вы хотите вложить'))
interest = int(input('под сокльок процентов')) / 100
time = int(input('сколько времени они будут лежать в банке'))

def bank(s, i =0.02,t=1):
    if i > 0.05:
        print('максимальный процент в нашем банке 5% годовых')
        return False
    total_savings = calc_savings(savings,interest,time)
    return total_savings

def calc_savings(savings,interest,time):
    for b in range(time):
        savings += savings*interest
    return savings

d = bank(savings,interest,time)
print(f'Ваш итоговый счет в банке: {d}')'''

def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
        user_guess = user_input()
        template = build_template(word_in_play, user_guess)
def build_template(t, w,g=''):

    for i in range(len(w)):
        if t[i] == '_':
            if w[i] == g:
                t[i] = w[i]
            else:
                t[i] = '_'
    return t
            
def user_input():
    '''
    output: return str, built-in input() function
    '''
    return input('введите строку:  ')
def welcome_speech(t):
    '''
    input: t - template(string)
    output: return none, used as just built-in function print()
    '''
    print(f'''
    Добро пожаловать в игру - hangman 2022
    Ваша задача угадать загаданное слово за несколько попыток,
    иначе вам конец.
    Загаданное слово состоит из {len(t)} букв {t}
    ''')
def start_template(w):
    '''
    inout: w - string(word)
    output: replace all chars in string to '_',
            return replaced chars as string with lengh w == t
    '''
    t = []
    for l in w:
        t.append('_')
    return t
def list_to_string_convert(t):
    '''
    input: t - template (list)
    output: s - list converted to string
    '''
    s = ''
    for g in t:
        s += '_'
    return s
def get_word(w):
    '''
    input: w - list with strings (words)
    output: for now: first element in list are string
            TODO: random string from list
    '''
    return w[0]


game()
