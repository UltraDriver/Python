__author__ = 'Рахматуллин Р.Р.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

n = 354
a = str(n)
for digits in a:
    print(digits)
while n >= 1:
    z = n % 10
    n //= 10
    print (z)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
x = input ("Введите переменную Х - ")
y = input ("Введите переменную У - ")
# Поменять значения переменных местами. Вывести новые значения на экран.
z = x
x = y
y = z
print ("X=", x, "Y=", y)
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


# Задача-3: Запросите у пользователя его возраст.
age =  int (input ("Сколько Вам лет? - "))
# Если ему есть 18 лет, выведите: "Доступ разрешен",
if age >= 18:
    print ("Доступ разрешен")
# иначе "Извините, пользование данным ресурсом только с 18 лет"
else:
    print ("Извините, пользование данным ресурсом только с 18 лет")