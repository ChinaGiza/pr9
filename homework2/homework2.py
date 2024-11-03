num1 = input(">>> Введите первое число: ")
num2 = input(">>> Введите второе число: ")

try:
    squares = []
    num1 = float(num1)
    num2 = float(num2)

    if num1 > num2:
        num1, num2 = num2, num1
    
    if num1 >= 0:
        num1 = int(num1) + 1
    else:
        if num1 == int(num1):
            num1 = int(num1) + 1
        else:
            num1 = int(num1)
    
    i = num1
    while i < num2:
        squares.append(i * i)
        i += 1
    
    print(f"### Результат: {squares}")
except:
    print("!!! Ошибка: введенные значения не являются числами")