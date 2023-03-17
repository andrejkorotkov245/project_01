# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!
arr = [4,6,2,1,9,63,-134,566]  
arr_2 = [-52, 56, 30, 29, -54, 0, -110]
arr_3 = [42, 54, 65, 87, 0] 
arr_4 = [5] 
arr_5 = [300] 

def minimum(arr):
    min=arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    i+=1
    return min
print(minimum(arr_4))

def maximum(arr):
    max=arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    i+=1
    return max
print(maximum(arr_4))