import random as rand

ticket = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

randomization = [0, 1, 2, 3, 4]
rand.shuffle(randomization)
win_combination = [rand.choice(ticket[i]) for i in randomization]

print("!!! Выберите и введите по одному числу из каждой строки следующей таблицы")
print("!!! Числа могут выбраны в любом порядке")
print("!!! Вводить в одну строк, разделяя числа пробелами")
for i in ticket:
    print(f"    {i[0]:2d} {i[1]:2d} {i[2]:2d} {i[3]:2d} {i[4]:2d}")
while True:
    try:
        user_combination = [int(i) for i in input(">>> Поле ввода: ").replace("  ", " ").split(" ") if i != ""]
        into = [0, 0, 0, 0, 0]
        for i in range(len(user_combination)):
            for j in range(len(ticket)):
                if user_combination[i] in ticket[j]:
                    into[i] = j
                    break
        if len(set(into)) < 5:
            print("!!! Внимание: Числа должны быть различны и принадлежать разным строкам таблицы")
        else:
            print(f"### Выиграшная комбинация: {win_combination}")
            print(f"### Комбинация пользователя: {user_combination}")
            percent = 0
            for i in range(5):
                if win_combination[i] == user_combination[i]:
                    percent += 20
            print(f"### Процент совпадения: {percent}")
            break
    except:
        print("!!! Ошибка: Введенное значение не является целым числом")