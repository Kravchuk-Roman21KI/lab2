users = {"roman": {"password": "1234",
    "grades": [12, 10, 8, 7, 11, 4, 9]},
    "ivan": {"password": "qwerty",
    "grades": [10, 9, 6, 8, 5, 3, 12]},
    "nazar": {"password": "1111",
   "grades": [7, 8, 4, 10, 11, 6] },
    "stanislav": {"password": "abcd",
   "grades": [12, 11, 10, 9, 8, 3, 2]}}
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:

    grades = users[login]["grades"]

    print("Вхід виконано успішно")
    print("Ваші оцінки:", grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("Кількість задовільних оцінок (5-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("Неправильний логін або пароль")
