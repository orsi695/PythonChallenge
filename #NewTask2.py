import re


def edit(file_in='C:/text.txt'):

    with open(file_in, 'r', encoding='utf8') as file:
        text = file.read()
        edited = re.findall(r'[а-яА-ЯёЁ]+', text)

        for i in range(len(edited) -1):
            if len(edited[i]) > 6:
                text = text.replace(edited[i], edited[i].title())

    print(text)

file_in = input("Введите путь до файла (C:/text.txt) -->  ")

edit()



