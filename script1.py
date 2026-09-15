users = {"roman": {"password": "1234",
    "ratings": [12, 10, 8, 7, 11, 4, 9]},
    "ivan": {"password": "qwerty",
    "ratings": [10, 9, 6, 8, 5, 3, 12]},
    "nazar": {"password": "1111",
   "ratings": [7, 8, 4, 10, 11, 6] },
    "stanislav": {"password": "abcd",
   "ratings": [12, 11, 10, 9, 8, 3, 2]}}
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:

    ratings = users[login]["ratings"]

    print("Вхід виконано успішно")
    print("Ваші оцінки:", ratings)

    satisfactory = 0
    unsatisfactory = 0

    for rating in ratings:
        if 4 <= rating <= 12:
            satisfactory += 1
        elif 1 <= rating <= 3:
            unsatisfactory += 1

    print("Кількість задовільних оцінок (4-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-3):", unsatisfactory)

else:
    print("Неправильний логін або пароль")
