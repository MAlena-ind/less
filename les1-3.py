# Задача 3. По введенным пользователем координатам 
# двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1, y1 = list(map(int, input('Введите координаты 1й точки, через пробел:  ').split()))
x2, y2 = list(map(int, input('Введите координаты 2й точки:  ').split()))

k = int((y1 - y2) / (x1 - x2))
b = y2 - k * x2

if b >= 0:
  print(f'y={k}x+{b}') 
else:
  print(f'y={k}x{b}')

  