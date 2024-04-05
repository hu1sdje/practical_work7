number = int(input())
while not int(number ** 0.5) ** 2 == number:
    print('Число не подходит! Введите другое!')
    number = int(input())
else:
    print('верно!')
