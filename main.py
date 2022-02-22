import os
import uuid
import shutil

class Book():
    def __init__(self):
        self.quantity_book = 0
        self.quantity_chapter = 0
        self.id = uuid.uuid4()

    def сounting_books(self, book):
        "Подсчет количества глав"
        self.quantity_chapter = 0

        for i in os.listdir(path=f'book/{book}/Главы'):
            self.quantity_chapter += 1

    def conclusion_book(self):
        print("В библтотеке сейчас есть такие книги:")
        for book_name in os.listdir(path='book'):
            print(f"Книга - {book_name}")
            for chapter_name in os.listdir(path=f'book/{book_name}/Главы'):
                print(f"  Глава - {chapter_name}")
            
            



    def сreating_book(self, name, chapter, text):
        "Создание книги"

        path = f'book\{name}'
        try:
            os.makedirs(path)
        except FileExistsError:
            print('Такая книга уже сужествует :(')
            exit()


        path = f'book\{name}\Главы'
        os.makedirs(path)

        text_file = open(f"book/{name}/Главы/{chapter}", "w", encoding='utf-8')
        text_file.write(f"{text}")
        text_file.close()

        Book.сounting_books(self, book)

        text_file = open(f"book/{name}/info.txt", "w", encoding='utf-8')
        text_file.write(f"ID Книги - {self.id}\nКоличество глав - {self.quantity_chapter}")
        text_file.close()



    def add_chapter(self, book, chapter, text):
        "Добавление глав к книге"
        for chapter_name in os.listdir(path=f'book\{book}\Главы'):
            if chapter_name == chapter:
                print("Такая глава уже существует :(")

        text_file = open(f"book/{book}/Главы/{chapter}", "w", encoding='utf-8')
        text_file.write(f"{text}")
        text_file.close()

        Book.сounting_books(self, book)

        text_file = open(f"book/{book}/info.txt", "w", encoding='utf-8')
        text_file.write(f"ID Книги - {self.id}\nКоличество глав - {self.quantity_chapter}")
        text_file.close()
            

        
    def rm_book(self, book):
        "Удаление книги"
        shutil.rmtree(f"book/{book}")
        Book.conclusion_book(self)

        Book.сounting_books(self, book)

        text_file = open(f"book/{book}/info.txt", "w", encoding='utf-8')
        text_file.write(f"ID Книги - {self.id}\nКоличество глав - {self.quantity_chapter}")
        text_file.close()


    def rm_chapter(self, book, chapter):
        "Удаление глав"
        try:
            os.remove(f"book/{book}/Главы/{chapter}")
        except FileNotFoundError:
            print('Такой главы нету :(')
            exit()
        Book.conclusion_book(self)

        Book.сounting_books(self, book)

        text_file = open(f"book/{book}/info.txt", "w", encoding='utf-8')
        text_file.write(f"ID Книги - {self.id}\nКоличество глав - {self.quantity_chapter}")
        text_file.close()

    def change_name_book(self, book, new_book):
        "Изменить название книги"
        try:
            os.rename(f"book/{book}", f"book/{new_book}")
        except FileNotFoundError:
            print('Такой книги нету :(')
            exit()

    def change_name_chapter(self, chapter, new_chapter, book):
        "Изменить название главы"
        try:
            os.rename(f"book/{book}/Главы/{chapter}", f"book/{book}/Главы/{new_chapter}")
        except FileNotFoundError:
            print('Такой главы нету :(')
            exit()

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
            choice_1 = int(input())
        except ValueError:
            print('Введите число !')
        else:
            loop_2 = False

    if choice_1 == 1:
        "Создание книги"
       

        name = input('Ведите название вашей книги: \n')
        chapter = input("Ведите название главы: \n")
        text = input(f"Введите текст, для гловы '{chapter}': \n")
        book_1.сreating_book(name, chapter, text)


    elif choice_1 == 2:
        "Добавление глав к книге"
        book_1.conclusion_book()

        book = input("К какой книге, хотите добавить новые главы:\n")

        chapter = input("Введите название новой главы: \n")
        text = input(f"Введите текст, для Вашей новой гловы: \n")
        book_1.add_chapter(book, chapter, text)


    elif choice_1 == 3:
        "Удаление книги"
        book_1.conclusion_book()
        book = input("Какую книгу хотите удалить ?:\n ")
        book_1.rm_book(book)

    elif choice_1 == 4:
        "Изменить название книги"
        book_1.conclusion_book()
        book = input("Какую книгу хотите переименовать:\n" )
        new_book = input(f"Ведите новое название, для книги {book}:\n" )
        book_1.change_name_book(book, new_book)

        book_1.conclusion_book()

    elif choice_1 == 5:
        "Изменить название главы"
        book_1.conclusion_book()

        chapter = input("Какую главу хотите переименовать:\n" )
        book = input("В какой книге находится эта глава ?:\n" )
        new_chapter = input(f"Ведите новое название, для главы {chapter}:\n" )

        book_1.change_name_chapter(chapter, new_chapter, book)
        book_1.conclusion_book()

    elif choice_1 == 6:
        "Удалить главу"
        book_1.conclusion_book()
        chapter = input("Какую главу хотите удолить ?:\n ")
        book = input("Введите название книги, в которой находится эта глава: \n")
        book_1.rm_chapter(book, chapter)

    elif choice_1 == 7:
        "Вывести информацию о всех существующих книгах"
        for book_name in os.listdir(path='book'):

            print(f"Книга - {book_name}")
            text_file = open(f"book/{book_name}/info.txt", "r", encoding='utf-8')
            for i in text_file:
                print(i)
            text_file.close()
            for chapter_name in os.listdir(path=f'book/{book_name}/Главы'):
                print(f"  Глава - {chapter_name}")

        

    elif choice_1 == 8:
        print("Выход из программы")
        exit()



