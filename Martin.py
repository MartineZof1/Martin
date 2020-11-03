#Martin Pavlenko 03.11.2020 №2
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

P = a + b + c

print("Периметр треугольника:",P)

#Martin Pavlenko 03.11.2020 №3
a=36.75
b=40
c=a/100*40
summa=3*(a-c)
print('Три товара со скидкой',summa)

#Martin Pavlenko 03.11.2020 №4
pizza=12.90
tips=10
c=pizza/100*10
summa=(pizza+c)/3
print('каждый заплатит', round(summa,2))

#Martin Pavlenko 03.11.2020 №5
a=29.9/60*24
print('Проедет за 24 мин, при средней сокрости 29,9км/ч: ')
print(round(a,2))


#Martin Pavlenko 03.11.2020 №6
import math
a=16
b=9
c=math.sqrt(a**2 + b**2)
print('гипотенуза', round(c,2))

#Martin Pavlenko 03.11.2020 №7
print('Введите первое число:')
dec=int(input())
b=bin(dec)
o=oct(dec)
h=hex(dec)
print(f'bin {b} | oct {o} | hex {h}')

#Martin Pavlenko 03.11.2020 №8
a=int(input('Введите чисило в десятичной системе\n'))
b=bin(a)
c=hex(a)
print(b,"\n",c)


#Martin Pavlenko 03.11.2020 №9
a=int(input('Ввести литры топлива: '))
b=int(input('Ввести пройденные километр: '))
result = a/b*100
print('Расход топлива на 100 км:',result)