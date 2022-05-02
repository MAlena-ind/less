# Задача 3-7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random


nms = [random.randint(-20, 30) for el in range(20)]

m1 = min(nms)
if nms.count(m1) > 1:
  m2 = m1
else:
  m2 = m1 + 1
  while True:
    if m2 in nms:
      break
    m2 += 1
print(f'Наименьшие элементы: {m1}, {m2}.')
    