# Задача 3-3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

m = [int(x) for x in input().split()]

a, b = m.index(min(m)), m[m.index(min(m))]
c, d = m.index(max(m)), m[m.index(max(m))]
m[a] = d
m[c] = b
 
print(m)
