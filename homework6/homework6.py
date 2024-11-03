import random as rand

size = 25
arr = [round(rand.random() * 200 - 100, 3) for i in range(size)]

try:
    arr = [float(i) for i in arr]

    max_elem = max(arr)
    min_elem = min(arr)

    print(f"### Максимальный элемент: {max_elem} \t Номер в списке: {arr.index(max_elem)}")
    print(f"### Минимальный элемент: {min_elem} \t Номер в списке: {arr.index(min_elem)}")

    print(f"### Список до изменений: {arr}")
    if max_elem == min_elem:
        print("!!! Внимание: взаимное замена мест между максимальным и минимальным элементами невозможно. Так как они равны друг другу")
    else:
        arr[arr.index(max_elem)], arr[arr.index(min_elem)] = arr[arr.index(min_elem)], arr[arr.index(max_elem)]
        print(f"### Сисок после изменений: {arr}")
except:
    print(f"!!! Ошибка: Введенное значение не является числом")