from fractions import Fraction
def view_data(data):
    print(data)

def get_value():
    return Fraction(input('Введите аргумент - '))

def get_action():
    return str(input('Введите необходимое действие(+ , - , * , /): '))

def help_rational():
    print('Ты выбрал РАЦИОНАЛЬНЫЕ числа, вводи числа дробные числа через "/" или "." и нажимай Enter.')

def help_kompleks():
    print('Ты выбрал КОМПЛЕКСНЫЕ числа, при вводе аргумента вводи действительную и мнимую часть через пробел и нажимай Enter.')

def get_value_komp():
    return list(map(int, input('Введите действительную и мнимую часть(через пробел): ').split()))