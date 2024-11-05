import re

email = input(">>> Введите свой e-mail: ")
matches = re.match(r"[a-zA-Z0-9\.\_\-]{1,}@[a-zA-Z0-9\.\-]{1,}\.[a-zA-Z]{2,}", email)

if matches:
    username = re.findall(r"[a-zA-Z0-9\.\_\-]{1,}@", email)
    domain = re.findall(r"@[a-zA-Z0-9\.\-]{1,}", email)
    print(f"### e-mail: {email}")
    print(f"### Имя пользователя: {username[0][:-1]}")
    print(f"### Доменное имя почты: {domain[0][1:]}")
else:
    print("!!! Ошибка: Введен некорректный e-mail")
