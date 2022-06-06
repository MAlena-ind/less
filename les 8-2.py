# Задача8-2.Закодируйте любую строку из трех слов по алгоритму Хаффмана.


from collections import Counter

# содание кода, кода шифрования и самого дерева

class Node:  
  """
  Класс Узел дерева.
  
  """
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value
    

def get_tree(s):
  """
  Функция построения дерева.
  
  """
  #  Если строка приходит пустая, возвращаем None
  if len(s) == 0:
    return None
  #  Посчитаем частоту каждого символа в пришедшей фразе.  
  count_s = Counter(s)
  #  Далее будем работать со отсортированным списком кортежей (каждый кортеж - это буква (или в процессе работы функции - экз.класса Node) и ее частотность)
  count_s = list(sorted(count_s.items(), key=lambda x: x[1], reverse=True))

  while len(count_s) >= 1:
    if len(count_s) == 1:
      a = count_s.pop()
      b = None
      a_b = a[1]
    else:
      a = count_s.pop()
      b = count_s.pop()
      a_b = a[1] + b[1]
    #   Возмем 2 кортежа из конца списка count_s с наиболее редко встречающимися элементами и оздадим объект Node со значением value = сумме частотности элементов от левой и правой веток Node 
      #  a и b - частотности элементов от левой и правой веток Node 
    n = Node(a_b, a, b)

    # Вставим получившуюся Node в отсортированный список кортежей count_s на место 
    # с сохранением возрастания по частотности. 0й элемент каждого котрежа - это либо строка (буква), либо элемент класса Node
    for i, val in enumerate(count_s):
      if a_b < val[1]:
        continue
      else:
        count_s.insert(i, (n, a_b))
        break
    # Или добавим Node в конец списка, если она имеет самую высокую частотность 
  count_s.append((n, a_b))
  # вернем Node, которая является корнем получившегося дерева
  return count_s[0][0]

  
def get_code(tree, codes={}, code=''):
  """
  Функция шифрования (рекурсивная).
  
  """
  if tree is None:
    return 'Объект не содержит символов.'
    # Создадим код для строки 
  if isinstance(tree, str):
    codes[tree] = code
    return codes
    # 0й элемент каждого котрежа - это либо строка (буква), либо элемент класса Node. 
  if tree.left:
    get_code(tree.left[0], codes, code=code + '1')
  if tree.right:
    get_code(tree.right[0], codes, code=code + '0')
  return codes


txt = get_code(get_tree(input('Введите текст: ')))

for b, k in txt.items():
  print(f'{b} - код {k}')
