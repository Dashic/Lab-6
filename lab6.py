#Вариант 8

import random

class Book:
    def __init__(self, num_pages, num_pictures):
        self.num_pages = num_pages
        self.num_pictures = num_pictures
        self.time_per_page = random.randint(1, 10)

    def reading_time(self):
        return self.num_pages * self.time_per_page

    def display_info(self):
        print(f"Количество страниц: {self.num_pages}, Время на прочтение: {self.num_pages * self.time_per_page}, Количество картинок: {self.num_pictures}")


class Encyclopedia(Book):
    def __init__(self, num_pages, num_pictures, num_articles_per_page, edition):
        super().__init__(num_pages, num_pictures)
        self.num_articles_per_page = num_articles_per_page
        self.time_per_page = random.randint(1, 10)
        self.edition = edition

    def articles_per_page(self):
        return self.num_articles_per_page

    def display_info(self):
        super().display_info()
        print(f"Количество статей на страницу: {self.num_articles_per_page}, Издание: {self.edition}")


class PhoneDirectory(Book):
    def __init__(self, num_pages, num_pictures, num_numbers_per_page, region):
        super().__init__(num_pages, num_pictures)
        self.num_numbers_per_page = num_numbers_per_page
        self.time_per_page = random.randint(1, 10)
        self.region = region

    def numbers_per_page(self):
        return self.num_numbers_per_page

    def display_info(self):
        super().display_info()
        print(f"Количество номеров на страницу: {self.num_numbers_per_page}, Регион: {self.region}")



encyclopedia1 = Encyclopedia(400, 40, 20, "Первое издание")
encyclopedia1.display_info()
print(f"Общее время чтения: {encyclopedia1.reading_time()} минут")

phone_dir1 = PhoneDirectory(75, 5, 7, "Европа")
phone_dir1.display_info()
print(f"Общее время чтения: {phone_dir1.reading_time()} минут")