# Задача 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Работаем с английским алфавитом.

n = int(input('Введите номер буквы от 1 до 26: '))

letter = chr(n + 96)
print(letter.upper(), letter)