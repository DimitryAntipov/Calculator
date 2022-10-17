import controller as c
vibor = int(input('Приветствую тебя ПОЛЬЗОВАТЕЛЬ,\n если ты хочешь посчитать рациональные числа введи "0",\n если ты хочешь вычеслить комплексные, то "1": \n'))
if vibor == 0:
    c.button_click_rational()
elif vibor == 1:
    c.button_click_kompleks()
else:
    print('Ошибка ввода!')