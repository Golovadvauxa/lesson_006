# -*- coding: utf-8 -*-

# Область видимости (scope) — это __текстовая__ территория в программе на Python,
# на которой прямым образом доступно пространство имён. 


def func_1():
    x = 34
    print('in f1 x =', x, 'locals() = ', locals())


x = 42
func_1()
print('x =', x)


# В любой момент во время выполнения существует как минимум три 
# вложенных области видимости, чьи пространства имён доступны:

# локальные имена - самая глубокая область видимости

# пространства имён всех заключающих [данный код] функций, 
# поиск по которым осуществляется начиная с ближайшей заключающей [код] 
# области видимости; 

# область видимости среднего уровня, по ней следующей проходит поиск 
# и она содержит глобальные имена текущего модуля; 

# и самая внешняя область видимости (заключительный поиск) — 
# это пространство имён, содержащее встроенные имена.

def func_2():
    def func_3():
        print('in func_3 x =', x)

    print('in func_2 x =', x)
    func_3()


x = 42
func_2()
print('x =', x)


###
# При вызове функций поиск имени  по стеку вызовов НЕ ПРОИСХОДИТ

def func_1():
    print('in func_1 x=', x)


def func_2():
    x = 'LOKO'
    print('in func_2 before call func_1 x=', x)
    func_1()


x = 'GLOBO'
func_2()


###
# области видимости текущего модуля

def f1():
    print('in f1 x =', x)


def f2():
    x = 'LOCO'
    print('in f2 x =', x)


def f3():
    def f4():
        print('in f3/f4 x =', x)
    f4()


def f5():
    def f6():
        print('in f5/f6 x =', x)
    x = 'LOCO-LOCO'
    f6()


x = 'GLOBO'
print('global x =', x)
f1()
f2()
f3()
f5()


###
# оператор nonlocal
def f1():
    def f2():
        nonlocal x
        x = 27
        print('in f2 x =', x)

    x = 34
    print('in f1 x =', x)
    f2()
    print('in f1 x =', x)


x = 42
f1()
print('x =', x)


# Особая хитрость в Python состоит в том, что
# — при условии, что в данной области не включены операторы global и nonlocal
# — присваивания именам всегда уходят в самое глубокое пространство имен.
# Присваивания не копируют данных — они лишь связывают имена с объектами. 







