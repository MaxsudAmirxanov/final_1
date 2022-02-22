import os
from random import choice
import uuid

class Book():
    def __init__(self):
        self.quantity_book = 0
        self.quantity_chapter = 0
        self.id = uuid.uuid4()

    def сounting_books(self, name):
        "Подсчет количества глав"
        for book_name in os.listdir(path='book'):
            self.quantity_book += 1

        for i in os.listdir(path=f'book/{name}'):
            self.quantity_chapter += 1
            print(i + "Подсчет глав")
            



    def сreating_book(self, name, chapter, text):
        "Создание книги"

        path = f'book\{name}'
        try:
            os.makedirs(path)
        except FileExistsError:
            print('Такая книга уже сужествует :(')
            exit()

        for i in os.listdir(path=f'book/{name}'):
            print(i)
            self.quantity_chapter += 1


        text_file = open(f"book/{name}/info.txt", "w", encoding='utf-8')
        text_file.write(f"ID Книги - {self.id}\nКоличество глав - {self.quantity_chapter}")
        text_file.close()


        path = f'book\{name}\Главы'
        os.makedirs(path)


        text_file = open(f"book/{name}/Главы/{chapter}", "w", encoding='utf-8')
        text_file.write(f"{text}")
        text_file.close()

        # path = f'book\{self.name}\{self.chapter}'
        # os.makedirs(path)

    def add_chapter(self):
        "Добавление глав к книге"
        
    def rm_book(self):
        "Удаление книги"

    def rm_chapter(self):
        "Удаление глав"

    def change_name_book(self):
        "Изменить название книги"

    def change_name_chapter(self):
        "Изменить название главы"

    def output_information_books():
        "Вывести информацию о всех существующих книгах"


book_1 = Book()


print("Добро пожаловать в электронную библтотеку, что Вы хотите сделать ?:")

loop_1 = True
while loop_1:

    
    print("""
    1) Создание книги
    2) Добавление глав к книге
    3) Удаление книги
    4) Изменить название книги
    5) Изменить название главы
    6) Удалить главу
    7) Вывести информацию о всех существующих книгах
    8) Выход из программы""")


    loop_2 = True
    while loop_2:
        try:
            choice = int(input())
        except ValueError:
            print('Введите число !')
        else:
            loop_2 = False

    if choice == 1:
        "Создание книги"
        name = input('Ведите название вашей книги: \n')
        chapter = input("Ведите название гловы: \n")
        text = input(f"Введите текст, для гловы '{chapter}': \n")
        book_1.сreating_book(name, chapter, text)


    elif choice == 2:
        "Добавление глав к книге"
        pass

    elif choice == 3:
        "Удаление книги"
        pass

    elif choice == 4:
        "Изменить название книги"
        pass

    elif choice == 5:
        "Изменить название главы"
        pass

    elif choice == 6:
        "Удалить главу"
        pass

    elif choice == 7:
        "Вывести информацию о всех существующих книгах"
        pass

    elif choice == 8:
        print("Выход из программы")
        exit()



