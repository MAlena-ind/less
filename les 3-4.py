# Задача 3-4. Определить, какое число в массиве встречается чаще всего.

# Создадим заполненный массив из 100 элементов натуральных чисел из диапазона до 50. 

import random
import collections

tpl =[round(random.random() * 51) for el in range(100)]
print(f'Чаще всего встречается число {collections.Counter(tpl).most_common(1)[0][0]}')