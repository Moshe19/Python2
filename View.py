from os import system
from msvcrt import getwch
import time


def menu(): 
    time.sleep(1)
    system('CLS') 
    move = {1: 'Создать контакт', 2: 'Прочитать книгу',
            3: 'Изменить контакт', 4: 'Удалить контакт', 5: 'Выход'}
    print('Выберите операцию', move)
    n = getwch()  
    if n.isdigit() and n in '12345':
        system('CLS')
        return int(n)
    else:
        system('CLS')
        print('Введите из предложенных вариантов')


def view(book):
    print('Список контактов телефонного справочника:\n')
    table = [['ФАМИЛИЯ', 'ИМЯ', 'ОТЧЕСТВО', 'НОМЕР ТЕЛЕФОНА']]
    for contact in book:
        contact = list(contact.values())
        table.append(contact)
    for i, item in enumerate(table):
        if i == 0:
            i = '№'
        print(i, '\t', *map(lambda x: str(x) + ' ' * (20 - len(x)), item))
    

def view2(book):
    key = 0
    if book == []:
        return
    table = [['ФАМИЛИЯ', 'ИМЯ', 'ОТЧЕСТВО', 'НОМЕР ТЕЛЕФОНА']]
    for contact in book:
        contact = list(contact.values())
        table.append(contact)
    while True:
        system('CLS')
        print('Список контактов телефонного справочника:\n')
        size = (len(table) + 3) // 5
        print(f'[{key + 1}/{size}]')
        print('№', '\t', *map(lambda x: str(x) +
              ' ' * (20
     - len(x)), table[0]))
        for ind, item in enumerate(table[key*5 + 1: key*5 + 6]):
            print(key*5 + ind + 1, '\t', *
                  map(lambda x: str(x) + ' ' * (20
         - len(x)), item))
        print('\nНажмите для просмотра   <- ->, a или d,    для выхода в меню - q')
        key_ch = getwch()
        if key_ch in 'фa' and key < size - 1:
            key += 1
        if key_ch in 'вd' and key > 0:
            key -= 1
        if key_ch in 'qй':
            break