# Задача 1. Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.
def sum_num(num):
  s = 0
  for i in list(str(num)):
    s += int(i)
  return s


def mul_num(num):
  m = 1
  for i in list(str(num)):
    m *= int(i)
  return m


n = int(input())
s = sum_num(n)
m = mul_num(n)
print('Сумма: ', s, ', Произведение: ', m)