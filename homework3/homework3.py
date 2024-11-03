odd_arr = []

print(">>> Начало ввода (введите 'end' для завершения):")
while True:
    input_var = input()
    if input_var == 'end':
        break
    else:
        try:
            input_var = int(input_var)
            if input_var % 2 == 1:
                odd_arr.append(input_var)
        except:
            print("!!! Ошибка: Введенное значение не является целым числом. Поэтому не добваляется в список")
print(">>> Конец ввода")

print(f"### Результат: {odd_arr}")