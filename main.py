import os
import uuid
import shutil

class Book():        
    def __init__(self, name_file_for_books):

        self.numer_of_chapters = 0
        self.id = uuid.uuid4()
        self.current_path = os.getcwd()
        self.data_dir_books = self.current_path + f'/{name_file_for_books}/'

    def file_name_books(self):
        return os.listdir(self.data_dir_books)
    
    def file_name_chapters(self, book_name):
        return os.listdir(self.data_dir_books + book_name + '/Chapters/')

    def counting_number_chapters(self, path):
        "Подсчет количества глав"
        self.numer_of_chapters = len(os.listdir(path))


    def update_info(self, book):
        "Обнавление файла info.txt"
        path = f'books/{book}/Chapters'
        self.counting_number_chapters(path)

        text_file = open(f"books/{book}/info.txt", "w", encoding='utf-8')
        text_file.write(f"ID Книги - {self.id}\nКоличество глав - {self.numer_of_chapters}")
        text_file.close()

    def сreating_book(self, name, chapter, text):
        "Создание книги"
        path = f'books\{name}'
        try:
            os.makedirs(path)
        except FileExistsError:
            print('Такая книга уже существует')

        path = f'books\{name}\Chapters'
        os.makedirs(path)

        self.add_chapter(name, chapter, text)
        self.update_info(name)

    def add_chapter(self, book, chapter, text):
        "Добавление глав к книге"
        try:
            text_file = open(f"books/{book}/Chapters/{chapter}", "w", encoding='utf-8')
        except FileNotFoundError:
            print('Такой книги не существует :(')
            exit()
        text_file.write(f"{text}")
        text_file.close()

        return chapter in os.listdir(path=f'books\{book}\Chapters')
 
    def rm_book(self, book):
        "Удаление книги"
        try:
            shutil.rmtree(f"books/{book}")
        except FileNotFoundError:
            print('Такой книги не существует :(')
            exit()

    def rm_chapter(self, book, chapter):
        "Удаление глав"   
        os.remove(f"books/{book}/Chapters/{chapter}")
        self.update_info(book)

    def change_name_book(self, book, new_book):
        "Изменить название книги"
        try:
            os.rename(f"books/{book}", f"books/{new_book}")
        except FileExistsError:
            print(' Такая книга уже существует :(')

    def change_name_chapter(self, chapter, new_chapter, book):
        "Изменить название главы"
        try:
            os.rename(f"books/{book}/Chapters/{chapter}", f"books/{book}/Chapters/{new_chapter}")
        except FileExistsError:
            print('Такая глава уже существует :(')

name_file_for_books = os.listdir()
book_1 = Book(name_file_for_books[1])

class Interface:
    def __init__(self, book):
        self.book = book
      
    def output_information_books(self, book_name):
        "Вывести информацию о всех существующих книгах"
        
        print(f"Книга - {book_name}")
        text_file = open(f"books/{book_name}/info.txt", "r", encoding='utf-8')
        for chapter_name in book_1.file_name_chapters(book_name):
            print(f"  Глава - {chapter_name}")
        for i in text_file:
            print(f" {i.strip()}")
        text_file.close()
        print("\n")

    def conclusion_book(self, books, current_path):
        "Вывод всех книг, и глав"
        for book in os.listdir(books):
            print('\n')
            print(book)
            data_dir_chapters = current_path + f'/books/{book}/Chapters'
            chapters = os.listdir(data_dir_chapters)
            for chapter in chapters:
                print(f"  {chapter}")
            

console = Interface(book_1)

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
        for book in os.listdir(path='books'):
            if name == book:
                print('Такая книга уже сужествует :(')
                exit()
        chapter = input("Ведите название главы: \n")
        text = input(f"Введите текст, для гловы '{chapter}': \n")              
        book_1.сreating_book(name, chapter, text) == False

    elif choice_1 == 2:
        "Добавление глав к книге"
        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book = input("К какой книге, хотите добавить новые главы:\n")
        chapter = input("Введите название новой главы: \n")
        text = input(f"Введите текст, для Вашей новой главы: \n")
        if book_1.add_chapter(book, chapter, text) == True:
            print("Такая глава уже существует :(")
        book_1.update_info(book)
        console.conclusion_book(book_1.data_dir_books, book_1.current_path)

    elif choice_1 == 3:
        "Удаление книги"
        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book = input("Какую книгу хотите удалить ?:\n ")
        book_1.rm_book(book)
        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book_1.update_info(book)

    elif choice_1 == 4:
        "Изменить название книги"
        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book = input("Какую книгу хотите переименовать:\n" )
        
        for name_book in os.listdir(path="books"):
            if name_book == book:
                new_book = input(f"Ведите новое название, для книги {book}:\n" )
                book_1.change_name_book(book, new_book)
                console.conclusion_book(book_1.data_dir_books, book_1.current_path)
                exit()
        else:
            print('Такой книги нету :(')
            exit()

    elif choice_1 == 5:
        "Изменить название главы"
        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book = input("В какой книге находится глава, которую хотите изменить ?:\n" )
        for name_book in os.listdir(path="books"):
            if name_book == book:
                chapter = input("Ведите название этой главы:\n" )
                for name_chapter in os.listdir(path=f"books/{book}/Chapters"):
                    if name_chapter == chapter:
                        new_chapter = input(f"Ведите новое название, для главы {chapter}:\n" )
                        book_1.change_name_chapter(chapter, new_chapter, book)
                        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
                        exit()
                else:
                    print('Такой главы нету :(')
                    exit()     
        else:
            print('Такой книги нету :(')
            exit() 

    elif choice_1 == 6:
        "Удалить главу"
        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book = input("Введите название книги, в которой находится эта глава: \n")
        for name_book in os.listdir(path="books"):
            if name_book == book:
                chapter = input("Какую главу хотите удолить ?:\n ")
                for name_chapter in os.listdir(path=f"books/{book}/Chapters"):
                    if name_chapter == chapter:
                        book_1.rm_chapter(book, chapter)
                        console.conclusion_book(book_1.data_dir_books, book_1.current_path)
                        exit()
                else:
                    print('Такой главы нету :(')
                    exit()     
        else:
            print('Такой книги нету :(')
            exit()        
        
    elif choice_1 == 7:
        "Вывести информацию о всех существующих книгах"
        for book_name in book_1.file_name_books():
            console.output_information_books(book_name)

    elif choice_1 == 8:
        print("Выход из программы")
        exit()
    
    else:
        print("Такого пункта нету :(")
        