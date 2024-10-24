from datetime import datetime
import json
import os
import json



class Book:
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year  # Новый атрибут для года издания
        self.genre = genre  # Новый атрибут для жанра

    def display_info(self):
        print(f"Название: {self.name}, Автор: {self.author}, Год: {self.year}, Жанр: {self.genre}")


    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year,
            "genre": self.genre
        }

books_dir = "library/books"
os.makedirs(books_dir, exist_ok=True)
books_json = os.path.join(books_dir, "books.json")

def чтение_бд(filename=books_json):
    books = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            books_data = json.load(file)  # Загружаем данные как словарь

            # Преобразуем словари обратно в объекты класса Book
            for name, data in books_data.items():
                # Создаём объекты класса Book для каждого элемента
                books[name] = Book(data['name'], data['author'], data['year'], data['genre'])

        print("Книги загружены из JSON, можно работать с библиотекой!")

    except FileNotFoundError:
        print("Файл не найден!")
    except PermissionError:
        print("Нет доступа к файлу!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    return books
#коммент

def добавить_книгу(books, user_name):
    while True:

        new_book = input("Введите название книги, или стоп для завершения: ")
        if new_book == "стоп":
            break
        elif new_book != "":
            count_books = len(books)
            print(count_books)
            if count_books > 7:
                print ("Количество введеных книг превысело лимита в 7 книг, вы не можете добавить больше!")
                break
            new_author = input("Введите имя автора книги: ") 
            while True:
                new_yers = input("Введите год выпуска книги: ")
                try:
                    new_yers = int(new_yers)
                    break
                except ValueError:
                    print("Значение не является числом!")

            new_genre = input("Введите жанр книги: ")
            log_action(f"Пользователь '{user_name}', добавил новую книгу со следующими параметрами: Название - '{new_book}', Автор - '{new_author}', Год издания - '{new_yers}' , Жанр - '{new_genre} '", user_name)
            books[new_book] = Book(new_book, new_author, new_yers, new_genre)
            print(f"Книга: {new_book}, Автора: {new_author}, {new_yers} года выпуска в жанре {new_genre}- успешно добавлена!")
            books[new_book].display_info()
        
        else:
            ("Не корректный ввод, повторите запрос!")

def просмотр_книги(books, user_name):
    if books:
        print("\nСписок книг")
        for i in books.values():
            i.display_info()
    else:
        print("\nКниг в бибилиотеке нет!")

def удалить_книгу(books, user_name):
    print("\nСписок книг в библиотеке: ")
    for i in books.values():
        i.display_info()
    while True:
        del_book = input("Введите название книги, которую хотите удалить, по завершению введите 'стоп': ")
        if del_book in books:
            del books[del_book]
            print(f"Книга {del_book} успешно удалена")
            log_action(f"Пользователь '{user_name}', удалил книгу  '{del_book}'", user_name)
        elif del_book == "стоп":
            log_action(f"Пользователь '{user_name}', вышел из меню удаления", user_name)
            break
        else:
            print("Книга не найдена, повторите ввод")

def сортировка_книг(books):
    while True:
        sort_type = input("Выберите критерий сортировки ('название', 'автор', 'год' или 'выход' для завершения): ").lower()
        if sort_type == "название":
            sorted_books = sorted(books.values(), key=lambda book: book.name)
            for book in sorted_books:
                book.display_info()
        elif sort_type == "автор":
            sorted_books = sorted(books.values(), key=lambda book: book.author)
            for book in sorted_books:
                book.display_info()
        elif sort_type == "год":
            sorted_books = sorted(books.values(), key=lambda book: int(book.year))
            for book in sorted_books:
                book.display_info()
        elif sort_type == "выход":
            print("Выход из сортировки")
            break
        else:
            print("Не верно введено значение, повторите ввод!")
            continue
    print("\nСписок отсорированных книгЖ")
    for book in sorted_books:
        book.display_info()



def поиск_книги(books, user_name):
    while True:
        search_type = input("Введите критерий поиска ('название', 'автор', 'жанр', 'год' или 'выход' для завершения): ").lower()
        if search_type == "название":
            search_value = input("Введите название для поиска: ").strip()
            found = False
            for book in books.values():
                if search_value.lower() in book.name.lower():
                    book.display_info()
                    log_action(f"Пользователь '{user_name}', успешно находит книгу '{search_value}'", user_name)
                    found = True
            if not found:
                print(f"Книга по введенному значению '{search_value}' не найдена")
                log_action(f"Пользователь '{user_name}', не нашел искомую книгу '{search_value}'", user_name)
        elif search_type == "автор":
            search_value = input("Введите автора для поиска: ").strip()
            found = False
            for book in books.values():
                if search_value.lower() in book.author.lower():
                    log_action(f"Пользователь '{user_name}', нашел книгу по автору '{search_value}'", user_name)
                    book.display_info()
                    found = True
            if not found:
                print(f"Книга по введенному значению '{search_value}' не найдена")
                log_action(f"Пользователь '{user_name}', не нашел книгу по автору '{search_value}'", user_name)
        elif search_type == "жанр":
            search_value = input("Введите жанр для поиска: ").strip()
            found = False
            for book in books.values():
                if search_value.lower() in book.genre.lower():
                    log_action(f"Пользователь '{user_name}', нашел книгу по жанру '{search_value}'", user_name)
                    book.display_info()
                    found = True
            if not found:
                print(f"Книга по введенному значению '{search_value}' не найдена")
                log_action(f"Пользователь '{user_name}', не нашел книгу по жанру '{search_value}'", user_name)
        elif search_type == "год":
            search_value = input("Введите год для поиска: ").strip()
            try:
                search_value = int(search_value)
                found = False
                for book in books.values():
                    if search_value == int(book.year):
                        log_action(f"Пользователь '{user_name}', нашел книгу по году '{search_value}'", user_name)
                        book.display_info()
                        found = True
                if not found:
                    print(f"Книга по введенному значению '{search_value}'год, не найдена")
                    log_action(f"Пользователь '{user_name}', не нашел книгу по году '{search_value}'", user_name)
            except ValueError:
                print("Год должен быть цифрами")
                log_action(f"Пользователь '{user_name}', ввел не верное значение в поиске по году '{search_value}'", user_name)
        elif search_type == "выход":
            log_action(f"Пользователь '{user_name}', вышел из поиска книг", user_name)
            break
        else:
            print("Не корректный ввод, попробуйте еще раз!")
            log_action(f"Пользователь '{user_name}', ввел не верное значение  '{search_type}'", user_name)

        







def изменить_книгу(books, user_name):
    print("\nСписок книг в библиотеке: ")
    for i in books.values():
        i.display_info()
    while True:
        choise = input("Что вы хотите изменить? Введите 'название', 'автор', 'год' или 'жанр', позавершению введите 'стоп': ").lower()
        if choise == "название":
                choise_name = input("Введите название книги которую хотите изменить: ")
                if choise_name in books:
                    while True:
                        new_choise = input("Введите новое название книги: ")
                        if new_choise is not None and new_choise.strip() != "":
                            books[new_choise] = books.pop(choise_name)
                            books[new_choise].name = new_choise
                            log_action(f"Пользователь '{user_name}', сдела изменение в названии кники с {choise_name} на '{new_choise}'", user_name)
                            print(f"Название книги изменилось с {choise_name} на {new_choise}")
                            break
                        else:
                            print("Название книги не может быть пустым, повторите ввод!")
                else:
                    print("Книга в библиотеке на найдена!")
        elif choise == "автор":
            choise_author = input("Введите название книги, автора книги которой вы хотите изменить: ")
            if choise_author in books:
                while True:
                    new_author = input(f"Введите нового автора для книги {choise_author}: ")
                    if new_author is not None and new_author.strip() != "":
                        books[choise_author].author = new_author
                        print(f"Автор книги '{choise_author}' успешно изменён на '{new_author}'.")
                        log_action(f"Пользователь '{user_name}', сдела изменение в книге {choise_author} Автора с {choise_name} на '{new_choise}'", user_name)
                        break
                    else:
                        print("Значение для автора не может быть пустым, повторите ввод!")
            else:
                print("Книга в библиотеке на найдена!")
        elif choise == "год":
            choise_year = input("Введите название книги, автора книги которой вы хотите изменить: ")
            if choise_year in books:
                while True:
                    new_year = input(f"Введиде измененный год для книги {choise_year}: ")
                    try:
                        new_year = int(new_year)
                        books[choise_year].year = new_year
                        print(f"Год для книги {choise_year} успешно изменен на {new_year}")
                        log_action(f"Пользователь '{user_name}', сдела изменение в книге '{choise_year}' года издания на '{new_year}'", user_name)
                        break
                    except ValueError:
                        print("Год должен быть числовым значением, повторите ввод!")
                    
            else:
                print("Книга в библиотеке на найдена!")
        elif choise == "жанр":
            choise_genre = input("Введите название книги жанр который вы хотите сменить: ")
            if choise_genre in books:
                while True:
                    new_genre = input(f"Введите новый жанр для книги {choise_genre}: ")
                    if new_genre is not None and new_genre.strip() != "":
                        books[choise_genre].genre = new_genre
                        print(f"Жанр для книги {choise_genre} успешно изменён на {new_genre}")
                        log_action(f"Пользователь '{user_name}', сдела изменение в книге '{choise_genre}' новый жано '{new_genre}'", user_name)
                        break
                    else:
                        print("Жанр не был изменён, введите корректный жанр.")
            else:
               print("Книга в библиотеке на найдена!")     
        elif choise == "стоп":
            log_action(f"Пользователь '{user_name}', вышел из меню редактирования книг", user_name)
            break
        
        else:
            print("Некорректный выбор! Повторите ввод!")

def сохранение_json(books, filename=books_json):
    book_save = {name: {"name": book.name, "author": book.author, "year": book.year, "genre": book.genre}
                for name, book in books.items()}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(book_save, file, ensure_ascii=False, indent = 4)
    print(f"Импорт библиотеке в форма json успешно завершон")

def сохранение_резерва(books, backup_dir = "backup"):
    os.makedirs(backup_dir, exist_ok=True)

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(backup_dir, f"backup_{current_time}.json")

    with open(backup_file, 'w', encoding='utf-8') as file:
        json.dump({name: book.to_dict() for name, book in books.items()}, file, ensure_ascii=False, indent=4)
    
    print(f"Резервная копия создана: {backup_file}")




def main_library_function(user_name):
    while True:
        command = input("Для работы с библиотекой введите: 'добавить', 'изменить', 'удалить', 'просмотр', 'поиск', 'сортировка', 'выйти': ").lower()
        if command == "добавить":
            добавить_книгу(books, user_name)
            log_action(f"Пользователь '{user_name}', выборал пункт '{command}'", user_name)
        elif command == "просмотр":
            просмотр_книги(books, user_name)
            log_action(f"Пользователь '{user_name}', выборал пункт '{command}'", user_name)
        elif command == "удалить":
            удалить_книгу(books, user_name)
            log_action(f"Пользователь '{user_name}', выборал пункт '{command}'", user_name)
        elif command == "изменить":
            изменить_книгу(books, user_name)
            log_action(f"Пользователь '{user_name}', выборал пункт '{command}'", user_name)
        elif command == "поиск":
            поиск_книги(books, user_name)
            log_action(f"Пользователь '{user_name}', выборал пункт '{command}'", user_name)
        elif command == "сортировка":
            сортировка_книг(books, user_name)
            log_action(f"Пользователь '{user_name}', выборал пункт '{command}'", user_name)
        elif command == "выйти":
            сохранение_json(books, user_name)
            сохранение_резерва(books)
            log_action(f"Пользователь '{user_name}', выборал пункт '{command}'", user_name)
            break
        else:
            print("Не корректный ввод, повторите запрос!")
print("До импорта лога")
from auth import log_action
print("после импорта лога")

print("Запуск авторизации...")
from auth import auth_user 
print("После импорта авторизации")
user_name = auth_user()
# Вызов функции авторизации
if user_name:
    print("Вход в библиотеку.....")
    books = чтение_бд()
    main_library_function(user_name)
    
else:
    print("Авторизация не пройдена.")


print(user_name)






