class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    класс пользователя, атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choise = input('Приветствую! Выберите действие:\n 1 - Вход \n 2 -Регистрация \n ')
        if choise == '1':
            login = input("Login: ")
            password = input("Pass: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен {login}')
                    break
                if password != database.data[login]:
                    print('Неверный пароль')
            else:
                print('Eror')
        if choise == '2':
            user = User(input("Login: "), password := input("Pass: "),
                        password_c := input("Con pass: "))
            if password != password_c:
                continue
            database.add_user(user.username, user.password)
        print(database.data)