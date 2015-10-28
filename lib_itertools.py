# -*- coding: utf-8 -*-


__author__ = 'mpak'

import itertools



c = itertools.count(10, 3)
#itertools.count() Ведет отсчет, если (10, 3) то от 10 с шагом 3

print(next(c))  #10
print(next(c))  #13
print(next(c))  #16
print(next(c))  #19



d = itertools.cycle([1, 2, 3])
#itertools.cycle() выдает значения по кругу
#например ([1, 2, 3]) будет давать 1, 2, 3, 1, 2, 3 и тд

print(next(d))  #1
print(next(d))  #2
print(next(d))  #3
print(next(d))  #1
print(next(d))  #2
print(next(d))  #3



e = itertools.permutations([1, 2, 3])
#itertools.permutations() выдает все возможные последовательности
#вывода данных

print(list(e))



f = itertools.combinations([1, 2, 3, 4, 5, 6], 2)
f2 = itertools.combinations([1, 2, 3, 4, 5, 6], 3)
#itertools.combinations() выдает все возможные комбинации
#вывода данных, вторым значением задаем размеры комбинаций

print(list(f))
print(list(f2))


g = itertools.product([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
#itertools.product() выдает все возможные комбинации
#вывода данных из двух и более списков

print(list(g))
