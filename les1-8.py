# Задача 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

a = input('Введите год нашей эры: ')

if a.isdigit():
  if int(a) % 4 == 0:
    print(f'Год {a} - високосный')
  else:
    print(f'Год {a} - невисокосный')
else:
  print('Год должен вводится цифрами, а не буквами.')