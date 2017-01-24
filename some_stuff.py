#!/usr/bin/python3.5


# ____Объединение в словарь)____

# a = ['sue']
# b = ['developer']
# c = dict(zip(a, b))
# print(c)

# ____Заполнение словаря пустого ____

# fields = ['name', 'job', 'age', 'pay']
# record = dict.fromkeys(fields, '?')
# print(record)

# ____ Исполнение комманд в терминале ____
# import sys, os
#
#
# sudo_password = input('Введи пароль \n')
# command = 'sudo apt-get update'
# p = os.system('echo {}|sudo -S {}' .format(sudo_password, command))
# print(p)
# ______________________________________
# import os
#
# mypass = input('Enter sudo passwd:\n')
# for k in os.popen('echo {}|sudo -S {}'.format(mypass, 'apt-get update')):
#     print(k)

# ____ os.startfile() ____
# Запускает файл стандартными средствами в операционке


# ____ with/as менеджер контекста ____
# with open('myfile.txt', 'r') as myfile, open('fout.txt', 'w') as fout:
#     for word in myfile:
#         fout.write(word)


