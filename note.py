import datetime

#класс заметки, с методом вывода заметки в консоль
class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def __str__(self):
        return f"ID: {self.id}\nЗаголовок: {self.title}\nТекст: {self.body}\nДата создания: {self.date}\n"