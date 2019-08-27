# -*- coding: utf-8 -*-
def say_hello(age):
    if age >= 18:
        print('Hola señor')
    else:
        print('Hola niño')

name = str(input('¿Cuál es tu nombre?'))

print('Hola, ' + name + '!')

age_input = int(input('¿Qué edad tiene?'))

say_hello(age_input)
