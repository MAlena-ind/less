# Задача 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

a = int(input('Сколько будет чисел в последовательности? '))
b = input('Считаем цифру: ')
c = 0

for i in range(1, a+1):
  c += input(f'Введите число {i}: ').count(b)

print(f'Цифра {b} встречается {c} раз.')