import numbers
import os
from turtle import numinput
import uuid

class Book():
    def __init__(self, name, chapter, text):
        self.name = name
        self.chapter = chapter
        self.text = text
        self.quantity_book = 0
        self.quantity_chapter = 0
        self.id = uuid.uuid4()

    def сounting_books(self):
        for book_name in os.listdir(path='book'):
            self.quantity_book += 1
            for chapter_name in book_name:
                self.quantity_chapter += 1



    def сreating_book(self):
        file = open(".book", 'w', encoding='utf-8')
        file.write(os.makedirs(f"{self.name}/{self.chapter}"))

        # text_file = open(f"{self.name}/info.txt", "w", encoding='utf-8')
        # text_file.write(f"ID Книги - {self.id}\nКоличество глав - ")
        # text_file.close()



# name = input('Ведите название вашей книги: \n')
# chapter = input("Ведите название гловы: \n")
# text = input(f"Введите текст, для гловы {chapter}: \n")


book_1 = Book("Война и мир_2", "Глова 1", "Тестовый текст")
book_1.сreating_book()
