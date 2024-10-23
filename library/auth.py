from datetime import datetime
import json
import os
class User:
    def __init__(self, id, user, pswd):
        self.id = id
        self.user = user
        self.pswd = pswd
    def to_dict(self):
        return{
            "id" : self.id,
            "user" : self.user,
            "pswd" : self.pswd
        }

def log_action(message, user_name, log_file = "auth.log"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_time}] {message}\n"
    log_dir = f"library/logs/"
    os.makedirs(log_dir, exist_ok=True)  # Создаём папку, если её нет

    log_file = f"{log_dir}/auth.log"
    with open(log_file, 'a') as file:
        file.write(log_message)


auth_dir = "library/auth"
os.makedirs(auth_dir, exist_ok=True)
auth_json = os.path.join(auth_dir, "auth.json")


def auth_user(file_auth=auth_json):
    auth_user = {}
    next_id = 1
    auth = False
    try:
        try:
            with open(file_auth, 'r') as file:
                auth_data = json.load(file)
        except FileNotFoundError:
            auth_data = {}
        user_name = input("Для доступа к библиотеке введите свое имя: ")
        if user_name in auth_data:
            while True:
                user_pswd = input("Введите ваш пароль: ")
                #for name, data in auth_data.items():
                if auth_data[user_name]["pswd"] == user_pswd:
                    print("Успешный вход, можете пользоватся библиотекой!")
                    log_action(f"Пользователь '{user_name}' успешно вошёл в систему.", user_name)
                    auth = True
                else:
                    print("Не верный пароль, повторите ввод!")
                    log_action(f"Пользователь '{user_name}' ввел не верный пароль.", user_name)

        else:
            print("Вы новый пользователь!")
            log_action(f"В систему заходит новый пользователь'{user_name}'.", user_name)
            next_id = len(auth_data) + 1
            while True:
                new_pswd = input("Придумайте пароль: ")
                check_new_pswd = input("Повторите ввод пароля: ")
                if new_pswd == check_new_pswd:
                    new_user_object = User(next_id, user_name, new_pswd)
                    auth_data[user_name] =new_user_object.to_dict()
                    with open(file_auth, 'w') as file:
                        json.dump(auth_data, file, indent=4, ensure_ascii=False)
                    print("Вы успешно зарегистрированы в программе.") 
                    log_action(f"Пользователь '{user_name}' успешно зарегистрировался.", user_name) 
                    auth = True
                    break
                else:
                    print("Введенные пароли не совпадают, повторите ввод")
    except Exception as e:
        print(f"Возникла ошибка {e}")


auth_user()