# Задача 3-1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

n = []

for i in range(2, 10):
  x = 0
  for j in range(2, 100):
    if j % i == 0:
      x += 1
  n.append([i, x])

[print(*m, sep='-') for m in n]
