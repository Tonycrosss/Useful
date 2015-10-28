# -*- coding: utf-8 -*-


__author__ = 'mpak'

# Этот итератор возвращает данные в обратном порядке

class Reverse:

    def __init__(self, data):

        self.data = data
        self.index = len(self.data)

    def __iter__(self):

        return  self

    def __next__(self):

        if self.index <= 0:
            raise StopIteration

        self.index -= 1
        return self.data[self.index]
        

#Проверяем 
r = Reverse('abcdef')

iterator = iter(r)
for x in iter(r):
    print(x)
