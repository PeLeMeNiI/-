money = int(input('введите по сколько скидываются:'))
people = int(input('введите количество людей'))
total_money = money * people
minimum_piz = people/2
total_piz = total_money//500
kvatit = minimum_piz * 500
if minimum_piz<total_piz:
    print('пиццы хватит')
else:
    print(f'пиццы не хватит, нехватило {kvatit - total_money}')
