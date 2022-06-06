# Задача8-1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.


import hashlib
import timeit
# import collections


def get_cnt_substring_hash(string):
  """
  Функция для определения количества различных подстрок в строке, с использованием хэш-функции

  """
    # Для хранения данных может использовтаься  defaultdict или множество. Множество работает чуть быстрее
  # d = collections.defaultdict(int) 
  l = set()
  for i in range(len(string) + 1):
    for j in range(i+1, len(string) + 1):
      hash = hashlib.md5(string[i:j].encode('utf-8'))
      l.add(hash.hexdigest())
      # d[hash.hexdigest()] += 1
  # return len(d.keys())
  return len(l)



# ТЕСТИРОВАНИЕ
s = 'iamgoingtogoforawalk'

n = timeit.timeit()
print(get_cnt_substring_hash(s))
print(timeit.timeit() - n)

# 201 - Количество уникальных подстрок
# 0.009051970000655274 - Время работы
