import random as rand

size = 10
arr = [round(rand.random() * 200 - 100, 3) for i in range(size)]

print(f"### Исходный список: {arr}")
for i in range(size):
    term = arr.pop(-1)
    arr.reverse()
    arr.append(term)
    arr.reverse()
    print(f"### Список со смещение +{i+1}: {arr}")