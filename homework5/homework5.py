import random as rand

size = 25
arr = [round(rand.random() * 200 - 100, 2) for i in range(size)]

try:
    arr = [float(i) for i in arr]

    more_than_previous = []
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            more_than_previous.append(arr[i])

    print(f"### Размер исходного списка: {size}")
    print(f"### Исходный список: {arr}")
    print(f"### Список с элементами, которые больше предыдущего элемента: {more_than_previous}")
except:
    print("!!! Ошибка: Введенное значение не является числом")