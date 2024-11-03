arr = []

print(">>> Начало ввода чисел (введите 'end' для завершения):")
while True:
    input_var = input()
    if input_var == 'end':
        break
    else:
        try:
            input_var = int(input_var)
            arr.append(input_var)
        except:
            print("!!! Ошибка: Введенное значение не является целым числом. Поэтому не добваляется в список")
print(">>> Конец ввода чисел")

even_count = 0
for i in arr:
    if int(i) % 2 == 0:
        even_count += 1

print(f"### Количество четных элементов: {even_count}")
print(f"### Количество нечетных элементов: {len(arr) - even_count}")