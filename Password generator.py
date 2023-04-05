import random

passw=[]

x='+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

try:
    a = int(input('Введи длину пароля: '))
    for i in range(a):
        symb = random.choice(x)
        passw.extend(symb)
    print('Сгенерирован пароль: ',"".join(passw))
except ValueError:
    print('Ошибка! Введи цифру')
