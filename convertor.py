import json

class Book:
    def __init__(self, id, name, author, year, genre):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre

# Конвертер для добавления ID в книги из старого JSON
def конвертировать_json_с_id(old_file='books.json', new_file='books_with_id.json'):
    books = {}
    next_id = 1

    try:
        # Чтение старого JSON файла
        with open(old_file, 'r', encoding='utf-8') as file:
            books_data = json.load(file)
            
            # Присваиваем каждому элементу уникальный ID
            for name, data in books_data.items():
                books[next_id] = Book(next_id, data['name'], data['author'], data['year'], data['genre'])
                next_id += 1
        
        # Преобразуем книги с ID в словари и записываем в новый JSON файл
        with open(new_file, 'w', encoding='utf-8') as json_file:
            books_to_save = {
                book.id: {
                    "id": book.id,
                    "name": book.name,
                    "author": book.author,
                    "year": book.year,
                    "genre": book.genre
                }
                for book in books.values()
            }
            json.dump(books_to_save, json_file, ensure_ascii=False, indent=4)

        print(f"Конвертация завершена. Книги с ID сохранены в {new_file}")
    
    except FileNotFoundError:
        print(f"Файл {old_file} не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск конвертера
конвертировать_json_с_id()
