"""Simulator program for studying and testing knowledge
 on the multiplication table"""

"""Программа-тренажер по изучению и проверки знаний по таблице умножения"""


from random import randint

# NUM - количество примеров в 1 тесте
NUM = 5
# Nmin - минимальная цифра умножения
Nmin = 2
# Всего решено примеров до выхода из режима теста
ALL = 0
# Всего ошибок до выхода из режима теста
MIS = 0
d = '*'
w = ' '
st = '_'


def trenazor():
    global ALL, MIS
    n = 0
    while True:
        a = randint(Nmin, 9)
        b = randint(Nmin, 9)
        print()
        if n != NUM:
            while True:
                p = input(f'{a} * {b} = ')
                p = p.replace(' ', '')
                c = a * b
                if p == '':
                    print()
                    print('Ошибка ввода! Введите ответ.')
                elif not p.isdigit():
                    print()
                    print('Ошибка ввода! Введите только цифры.')
                elif p.isdigit():
                    if int(p) == c:
                        print(f'Верно!')
                        n += 1
                        ALL += 1
                        break
                    if int(p) != c:
                        print(f'Ошибка! Правильный ответ: {c}')
                        n += 1
                        ALL += 1
                        MIS += 1
                        break
        elif n == NUM:
            pros = (ALL - MIS)/ALL * 100
            while True:
                print(34 * st)
                print('Ваш выбор:')
                print('  1.Продолжить тест')
                print('  2.Вернуться на главное Меню')
                print('  3.Выйти из программы')
                print(34 * st)
                t = input('Введите цифры (1, 2 или 3): ')
                t = t.replace(' ', '')
                if t == '1':
                    trenazor()
                    break
                elif t == '2':
                    print()
                    print(32 * d + f'  ВАШ РЕЗУЛЬТАТ: {pros: .0f} %  ' + 32 * d)
                    print(30 * d + f'  Всего решено: {ALL} примеров  ' + 30 * d)
                    print(35 * d + f'  Ошибок: {MIS} шт.  ' + 35 * d)
                    main()
                    break
                elif t == '3':
                    print()
                    print(32*d + f'  ВАШ РЕЗУЛЬТАТ: {pros: .0f} %  ' + 32*d)
                    print(30*d + f'  Всего решено: {ALL} примеров  ' + 30*d)
                    print(35*d + f'  Ошибок: {MIS} шт.  ' + 35*d)
                    print()
                    print('Программа "Тренажер таблицы умножения" ЗАКРЫТА.')
                    exit()
                elif t == '':
                    print()
                    print('Ошибка! Введите значение')
                else:
                    print()
                    print('Ошибка ввода! Введите цифры.')


def tablisa():
    print()
    print(w*8 + 'Таблица умножения')
    print(34*st)
    for i in range(1, 10):
        for g in range(1, 10):
            print(i*g, end='\t')
        print()
    print(34*st)
    while True:
        print('Ваш выбор:')
        print('   1.Вернуться на главное Меню')
        print('   2.Выйти из программы')
        print(34 * st)
        t1 = input('Введите цифры (1 или 2): ')
        t1 = t1.replace(' ', '')
        if t1 == '1':
            main()
            break
        elif t1 == '2':
            print()
            print('Программа "Тренажер таблицы умножения" ЗАКРЫТА.')
            exit()
        elif t1 == '':
            print()
            print('Ошибка ввода! Введите значение.')
        else:
            print()
            print('Ошибка ввода! Введите только цифры.')


def main():
    global ALL, MIS
    ALL = 0
    MIS = 0
    print(53*st)
    print('Это программа: "Тренажер таблицы умножения" (v 1.0)')
    print('''  Выберите из меню:
    1. Показать таблицу умножения
    2. Запустить тренажер
    3. Выйти из программы''')
    print(53 * st)
    while True:
        t3 = input('Введите ваш выбор (цифра 1, 2 или 3): ')
        t3 = t3.replace(' ', '')
        if t3 == '1':
            tablisa()
            break
        elif t3 == '2':
            trenazor()
            break
        elif t3 == '3':
            print()
            print('Программа "Тренажер таблицы умножения" ЗАКРЫТА.')
            exit()
        elif t3 == '':
            print()
            print('Ошибка ввода! Введите значение.')
        else:
            print()
            print('Ошибка ввода! Введите только цифры.')


if __name__ == '__main__':
    main()