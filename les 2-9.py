# Задача 2-9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

nums = list(map(int, input('Введите через пробел несколько натуральных чисел: ').split()))
max_num = 0
max_sum = 0

for i, d in enumerate(nums):
  s = 0
  while d > 0:
    s += d % 10
    d //= 10
  if s > max_sum:
    max_sum = s
    max_num = nums[i]

print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}.')