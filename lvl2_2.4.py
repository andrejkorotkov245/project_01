# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
print('\nПункт A')
s = "Hi! Hello!"
s1 = "Oh, no!!!"
s2 = ""
def remove_exclamation_marks(s):
    s = s.replace('!', '')
    return s

print(remove_exclamation_marks(s))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
print('\nПункт B')
s3 = "Hi!!!"

len = len(s3)

def split(s): #Функция разбиения строки в список
    return [char for char in s]

def remove_last_em(s): #Функция удаления последнего знака !
    splitted = (split(s))
    if splitted[len-1] == '!':
        splitted.pop(len-1)
    return(''.join(splitted))

print(remove_last_em(s3)) #Выводим результат

               
# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

print('\nПункт С')
s4 = ("!Hi! Hi! Hi!")
new_list=[]

def calc_list_length(list): #Вспомогательная функция получения кол-ва эл-в в списке
    counter = 0
    for i in list:
        counter=counter+1
    return counter

def remove_word_with_one_em(s): #Функция удаления слов содержащих ровно один восклицательный знак
    for i in range(calc_list_length(s.split())):
        if s.split()[i].count('!') != 1:     #определяем кол-во знаков восклицания в каждом элементе списка и сравниваем с 1
            new_list.append(s.split()[i])    #наполняем new_list такими значениями, в которых знаков восклицания не один
    return(new_list)

print(remove_word_with_one_em(s4))


          