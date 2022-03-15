import os
import uuid
import shutil

class Book():

    @staticmethod
    def conclusion_book(books, current_path):
        "Вывод всех книг, и глав"

        for book in os.listdir(books):
            print(book)

            data_dir_chapters = current_path + f'/books/{book}/Главы'
            chapters = os.listdir(data_dir_chapters)
            for chapter in chapters:
                print(chapter)
                
                # return True, book, chapters
                
    def __init__(self):

        self.count = 0
        self.id = uuid.uuid4()
        self.current_path = os.getcwd()
        self.data_dir_books = self.current_path + '/books/'
    
    def counting_number_chapters(self, path):
        "Подсчет количества глав"
        self.count = 0
        for i in os.listdir(path):
            self.count += 1

    def update_info(self, book):
        "Обнавление файла info.txt"
        path = f'books/{book}/Главы'
        self.counting_number_chapters(self, path)

        text_file = open(f"books/{book}/info.txt", "w", encoding='utf-8')
        text_file.write(f"ID Книги - {self.id}\nКоличество глав - {self.count}")
        text_file.close()



    def сreating_book(self, name, chapter, text):
        "Создание книги"
        path = f'books\{name}'
        os.makedirs(path)

        path = f'books\{name}\Главы'
        os.makedirs(path)

        text_file = open(f"books/{name}/Главы/{chapter}", "w", encoding='utf-8')
        text_file.write(f"{text}")
        text_file.close()

        self.update_info(self, name)


    def add_chapter(self, book, chapter, text):
        "Добавление глав к книге"
        for chapter_name in os.listdir(path=f'books\{book}\Главы'):
            if chapter_name == chapter:
                return False

        text_file = open(f"books/{book}/Главы/{chapter}", "w", encoding='utf-8')
        text_file.write(f"{text}")
        text_file.close()

     
    def rm_book(self, book):
        "Удаление книги"
        shutil.rmtree(f"books/{book}")


    def rm_chapter(self, book, chapter):
        "Удаление глав"
        
        os.remove(f"books/{book}/Главы/{chapter}")
        self.conclusion_book(self.data_dir_books, self.current_path)
        self.update_info(self, book)


    def change_name_book(self, book, new_book):
        "Изменить название книги"
        os.rename(f"books/{book}", f"books/{new_book}")


    def change_name_chapter(self, chapter, new_chapter, book):
        "Изменить название главы"
        os.rename(f"books/{book}/Главы/{chapter}", f"books/{book}/Главы/{new_chapter}")

    def output_information_books(self, book_name):
        "Вывести информацию о всех существующих книгах"
        
        print(f"Книга - {book_name}")
        text_file = open(f"books/{book_name}/info.txt", "r", encoding='utf-8')
        chapter_name = os.listdir(path=f'books/{book_name}/Главы')
        # for chapter_name in os.listdir(path=f'books/{book_name}/Главы'):
        #     # print(f"  Глава - {chapter_name}")
            
            
        for i in text_file:
            # print(f" {i.strip()}")
            pass
        
        text_file.close()
        # print("\n")
        return text_file, chapter_name
        





book_1 = Book()

class Interface:
    def __init__(self, book_1):
        self.book_1 = book_1
        
    def output_information_books_Interface(self, book_name):
        "Вывести информацию о всех существующих книгах Interface"
        
        choice = book_1.output_information_books(book_name)
        print(f"Книга - {book_name}")
        for chapter_name in choice[1]:
            print(chapter_name)
            
        for info in choice[0]:
            print(f" {info.strip()}")
        # print(choice[0])
        # print(choice[1])
        # print('---')

        # if choice[0] == "Глава":
        #     print(f"  Глава - {choice[1]}")
    def conclusion_book_Interface(self):
        choice = book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)
        print(choice)
        print(choice[1])
        print(f"  Глава - {choice[2]}")
        if choice[0] == True:
            for i in book_1.conclusion_book(book_1.data_dir_books, book_1.current_path):
                print(i)


        
    


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
        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)

        book = input("К какой книге, хотите добавить новые главы:\n")

        chapter = input("Введите название новой главы: \n")
        text = input(f"Введите текст, для Вашей новой гловы: \n")
        if book_1.add_chapter(book, chapter, text) == False:
            print("Такая глава уже существует :(")
        book_1.update_info(book)

    elif choice_1 == 3:
        "Удаление книги"
        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book = input("Какую книгу хотите удалить ?:\n ")
        book_1.rm_book(book)
        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book_1.update_info(book)

    elif choice_1 == 4:
        "Изменить название книги"
        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)
        book = input("Какую книгу хотите переименовать:\n" )
        for name_book in os.listdir(path="books"):
            if name_book != book:
                print('Такой книги нету :(')
                exit()
        new_book = input(f"Ведите новое название, для книги {book}:\n" )
        book_1.change_name_book(book, new_book)

        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)

    elif choice_1 == 5:
        "Изменить название главы"
        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)


        book = input("В какой книге находится глава, которую хотите изменить ?:\n" )
        for name_book in os.listdir(path="books"):
            if name_book == book:
                chapter = input("Ведите название этой главы:\n" )
                for name_chapter in os.listdir(path=f"books/{book}/Главы"):
                    if name_chapter == chapter:
                        new_chapter = input(f"Ведите новое название, для главы {chapter}:\n" )

                        book_1.change_name_chapter(chapter, new_chapter, book)
                        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)
                else:
                    print('Такой главы нету :(')
                    exit()     
        else:
            print('Такой книги нету :(')
            exit() 

    elif choice_1 == 6:
        "Удалить главу"
        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)

        book = input("Введите название книги, в которой находится эта глава: \n")
        for name_book in os.listdir(path="books"):
            if name_book == book:
                chapter = input("Какую главу хотите удолить ?:\n ")
                for name_chapter in os.listdir(path=f"books/{book}/Главы"):
                    if name_chapter == chapter:
                        book_1.rm_chapter(book, chapter)
                        book_1.conclusion_book(book_1.data_dir_books, book_1.current_path)
                else:
                    print('Такой главы нету :(')
                    exit()     
        else:
            print('Такой книги нету :(')
            exit()        
        
    elif choice_1 == 7:
        "Вывести информацию о всех существующих книгах"
        # for book_name in os.listdir(path='books'):
        #     # book_1.output_information_books(book_name)
        #     console.output_information_books_Interface(book_name)

        # data_dir_chapter = current_path + '/books/' #Наш путь к книгам
        current_path = os.getcwd()
        data_dir_books = current_path + '/books/' #Наш путь к книгам
        data_books = os.listdir(data_dir_books) #Наши файлы
        # book_1.conclusion_book(data_books, current_path)
        console.conclusion_book_Interface()

    elif choice_1 == 8:
        print("Выход из программы")
        exit()
    
    else:
        print("Такого пункта нету :(")



