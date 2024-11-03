import re

email = input(">>> Введите свой e-mail: ")
matches = re.match(r"[a-z0-9\.]{1,100}@[a-z0-9\.]{1,100}", email)

if matches:
    username = re.findall(r"[a-z0-9\.]{1,100}@", email)
    domain = re.findall(r"@[a-z0-9\.]{1,100}", email)
    print(f"### e-mail: {email}")
    print(f"### Имя пользователя: {username[0][0:-1]}")
    print(f"### Доменное имя почты: {domain[0][1:]}")
else:
    print("!!! Ошибка: e-mail содержит символы, не являющиеся точкой (.) и не принадлежащие a-z и 0-9")