#Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит 
#их к строке и отдает объединенными через разделитель delimiter
#Вызовите функцию, передав в нее два аргумента "Learn" и "python",
#положите результат в переменную и выведите ее значение на экран
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами
def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimeter = str('&')
    return str(one+ delimeter +two)


summ = get_summ('learn','python').upper()
print (summ)

#Задание 2 Функции
#Создайте в редакторе файл price.py
#Создайте функцию format_price, которая принимает один аргумент price
#Приведите price к целому числу (тип int)
#Верните строку "Цена: ЧИСЛО руб."
#Вызовите функцию, передав на вход 56.24 и положите результат в переменную
#Выведите значение переменной с результатом на экран

def format_price(price):
    price= int(price)
    return f'Цена: + {price} + рубли'




a=format_price(56.24)
print(a)   



