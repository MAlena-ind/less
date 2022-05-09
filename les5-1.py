# Задача5-1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections


def data_process_comps(companies):
  """
  Функция для расчета средней годовой прибыли ряда предприятий 
  и разделение данного ряда компаний на 2 группы, чья прибыль выше и ниже средней. 
  Функция принимает аргумент типа данных "словарь" 
  (компания: годовой оборот)"""
  counter = collections.Counter(companies)
  avrg = round(sum(counter.values())/len(counter.keys()), 2) #средняя годова прибыль
  d_c = dict(counter) 
  res = f'Средняя прибыль за год для всех предприятий: {avrg}.\nКомпании, прибыль которых выше либо равна средней: {", ".join([i for i in d_c if d_c[i] >= avrg])}.\nКомпании, прибыль которых ниже средней: {", ".join(list(filter(lambda i:d_c[i] < avrg, d_c)))}'
  return res  


cnt = int(input('Введите количество предприятий: '))
companies = {}
i = 1

while cnt > len(companies):
  company = input(f'Введите название компании {i} и ее прибыль за каждый квартал года (через пробел): ').split()
  companies[company[0]] = sum(int(i) for i in company[1:])
  i += 1

print(data_process_comps(companies))
