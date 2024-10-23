from datetime import datetime
import json
import os
class Book:
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year  # Новый атрибут для года издания
        self.genre = genre  # Новый атрибут для жанра

    def display_info(self):
        print(f"Название: {self.name}, Автор: {self.author}, Год: {self.year}, Жанр: {self.genre}")
import json
#wdaawdad

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

def добавить_книгу(books):
    while True:

        new_book = input("Введите название книги, или стоп для завершения: ")
        if new_book == "стоп":
            break
        elif new_book != "":
            new_author = input("Введите имя автора книги: ") 
            while True:
                new_yers = input("Введите год выпуска книги: ")
                try:
                    new_yers = int(new_yers)
                    break
                except ValueError:
                    print("Значение не является числом!")

            new_genre = input("Введите жанр книги: ")

            books[new_book] = Book(new_book, new_author, new_yers, new_genre)
            print(f"Книга: {new_book}, Автора: {new_author}, {new_yers} года выпуска в жанре {new_genre}- успешно добавлена!")
            books[new_book].display_info()
        
        else:
            ("Не корректный ввод, повторите запрос!")

def просмотр_книги(books):
    if books:
        print("\nСписок книг")
        for i in books.values():
            i.display_info()
    else:
        print("\nКниг в бибилиотеке нет!")

def удалить_книгу(books):
    print("\nСписок книг в библиотеке: ")
    for i in books.values():
        i.display_info()
    while True:
        del_book = input("Введите название книги, которую хотите удалить, по завершению введите 'стоп': ")
        if del_book in books:
            del books[del_book]
            print(f"Книга {del_book} успешно удалена")
        elif del_book == "стоп":
            break
        else:
            print("Книга не найдена, повторите ввод")


def поиск_книги(books):
    while True:
        search_type = input("Введите критерий поиска ('название', 'автор', 'жанр', 'год' или 'выход' для завершения): ").lower()
        if search_type == "название":
            search_value = input("Введите название для поиска: ").strip()
            found = False
            for book in books.values():
                if search_value.lower() in book.name.lower():
                    book.display_info()
                    found = True
            if not found:
                print(f"Книга по введенному значению '{search_value}' не найдена")
        elif search_type == "автор":
            search_value = input("Введите автора для поиска: ").strip()
            found = False
            for book in books.values():
                if search_value.lower() in book.author.lower():
                    book.display_info()
                    found = True
            if not found:
                print(f"Книга по введенному значению '{search_value}' не найдена")
        elif search_type == "жанр":
            search_value = input("Введите жанр для поиска: ").strip()
            found = False
            for book in books.values():
                if search_value.lower() in book.genre.lower():
                    book.display_info()
                    found = True
            if not found:
                print(f"Книга по введенному значению '{search_value}' не найдена")
        elif search_type == "год":
            search_value = input("Введите год для поиска: ").strip()
            try:
                search_value = int(search_value)
                found = False
                for book in books.values():
                    if search_value == int(book.year):
                        book.display_info()
                        found = True
                if not found:
                    print(f"Книга по введенному значению '{search_value}'год, не найдена")
            except ValueError:
                print("Год должен быть цифрами")
        elif search_type == "выход":
            break
        else:
            print("Не корректный ввод, попробуйте еще раз!")

        







def изменить_книгу(books):
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
                        break
                    else:
                        print("Жанр не был изменён, введите корректный жанр.")
            else:
               print("Книга в библиотеке на найдена!")     
        elif choise == "стоп":
            break
        
        else:
            print("Некорректный выбор! Повторите ввод!")

def сохранение_json(books, filename=books_json):
    book_save = {name: {"name": book.name, "author": book.author, "year": book.year, "genre": book.genre}
                for name, book in books.items()}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(book_save, file, ensure_ascii=False, indent = 4)
    print(f"Импорт библиотеке в форма json успешно завершон")



books = чтение_бд()


while True:
    command = input("Для работы с библиотекой введите: 'добавить', 'изменить', 'удалить', 'просмотр', 'поиск', 'выйти': ").lower()
    if command == "добавить":
        добавить_книгу(books)
    elif command == "просмотр":
        просмотр_книги(books)
    elif command == "удалить":
        удалить_книгу(books)
    elif command == "изменить":
        изменить_книгу(books)
    elif command == "поиск":
        поиск_книги(books)
    elif command == "выйти":
        сохранение_json(books)
        break
    else:
        print("Не корректный ввод, повторите запрос!")