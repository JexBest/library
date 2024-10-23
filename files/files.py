with open("file.txt", 'w') as file:
    file.write("Залупка\n")
    file.write("Нежная\n")


print("Файл успешно записан")

try:
    with open("file.txt", 'r') as file:
        content = file.read()
except FileExistsError:
    print("Файл не найден!")


print(content)

with open("file.txt", 'a') as file:
    file.write("А это я добавил после\n")
print("добавлена новая строка")


with open("file.txt", 'r') as file:
    for line in file:
        print("Строка из файла", line.strip())