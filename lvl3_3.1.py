# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)


from sys import stdin

class Matrix:

    def __init__(self, dims, fill):
       self.rows = dims[0]
       self.columns = dims[1]
       self.A = [[fill] * self.columns for i in range(self.rows)]
   
    def __str__(self):
       m = len(self.A)
       mtxStr = ''
       for i in range(m):
            mtxStr += ('|' + ','.join(map(lambda x:'{}'.format(x), self.A[i])) + '| \n')
       return mtxStr

    
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
             i = key[0]
             j = key[1]
             self.A[i][j] = value

    def size(self):
        size = (len(self.A), len(self.A[0]))
        return size
    
    def newcolumn(self, b):
        m = len(self.A)
        print('---Расширенная матрица---')
        for i in range(m):
            print (self.A[i] + b)
        
#---------------------------------- Проверяем созданный класс Matrix и параллельно проявляем фантазию:--------------------------------------

#1)Спрашиваем пользователя размер матрицы и чем заполнить её
rws = int (input('Введите желаемое количество строк матрицы от 1 до n: '))
cls = int (input('Введите желаемое количество столбцов матрицы от 1 до n: '))
nums = int (input('Каким числом будем заполнять?: '))

#2)Выводим результат
M = Matrix(dims = (rws,cls), fill = nums)
print(M)

#3)Заменяем определённый элемент матрицы через диалог
que = str (input(f'Хотите что-нибудь заменить в этой отличной матрице? y/n: '))
if que=='y' or que=='yes' or que=='Y' or que=='Yes' or que=='YES':
    x = int(input(f'А какой номер по вертикали? '+'Учтите максимум='+str(cls)+': '))
    y = int(input(f'А какой номер по горизонтали? '+'Учтите максимум='+str(rws)+': '))
    change = int(input(f'Какой цифрой заменить? '))
    print("Ок. Заменяю...")
    print('---Результат---')
    M[x-1,y-1] = change
    print(M)
else:
    print('Ну нет так нет')

#4)Считаем кол-во  столбцов и строк
print('В текущей матрице '+str(M.size()[0]) + ' строк'+' и '+ str(M.size()[1]) + ' столбцов')

#5)Добавляем столбик в текущую матрицу
que = str (input(f'Хотите добавить столбик в этой отличной матрице? y/n: '))
if que=='y' or que=='yes' or que=='Y' or que=='Yes' or que=='YES':
    b = int(input(f'Из какой цифры должен состоять доп.столбик справа?: '))
    M.newcolumn([b])
else:
    print('Ну как хотите')

