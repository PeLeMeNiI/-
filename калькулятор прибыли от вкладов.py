procent = int(input('введите процент прибыли:'))
summ = int(input('введите сумму, которую вы даете банку:'))
years = int(input('введите срок, на который деньги останутся у банка:'))
num_of_year = 0
money = 0
for i in range(years):
    money = (summ/100 * procent) + summ
    summ = money
    num_of_year += 1
    print(f'{num_of_year} год. у вас будет {money} рублей.')
