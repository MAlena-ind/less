# Задача 3-5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# Создадим заполненный массив из 100 элементов натуральных чисел из диапазона до -100 до 100. 
import random

# можно использовать () и работать с генераторным объектом
tpl =[random.randint(-100, 101) for el in range(100)]
min_num = 0

for i, x in enumerate(tpl):
  if x < min_num:
    min_num = x
    ind = i + 1

print(f'Отрицательных чисел нет.' if min_num == 0 else 
      f'Максимальный отрицательный элемент: {min_num}, позиция в массиве: {ind}.')