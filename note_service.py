import json
import csv

class NoteService:
    def __init__(self, filename):
        self.filename = filename
        
    #создание заметки
    def create_note(self):
        id = input("Введите идентификатор заметки: ")
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note = Note(id, title, body, date)
        self.save_note_to_file(note)

        print("Заметка успешно создана!")
        
        
    #поиск и вывод заметки
    def read_notes(self):
        filter_date = input("Введите дату для фильтрации (YYYY-MM-DD): ")

        notes = self.load_notes_from_file()
        for note in notes:
            if filter_date == "" or filter_date == note.date[:10]:
                print(note)
                

    #редактирование заметки
    def edit_note(self):
        id = input("Введите идентификатор заметки: ")

        notes = self.load_notes_from_file()
        for i in range(len(notes)):
            if notes[i].id == id:
                print(notes[i])
                new_title = input("Введите новый заголовок (оставьте пустым, если не хотите менять): ")
                if new_title != "":
                    notes[i].title = new_title

                new_body = input("Введите новый текст (оставьте пустым, если не хотите менять): ")
                if new_body != "":
                    notes[i].body = new_body

                notes[i].date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.save_notes_to_file(notes)

                print("Заметка успешно изменена!")
                return

        print("Заметка с таким идентификатором не найдена!")
        
        
    #удаление заметки
    def delete_note(self):
        id = input("Введите идентификатор заметки: ")

        notes = self.load_notes_from_file()
        for i in range(len(notes)):
            if notes[i].id == id:
                del notes[i]

                self.save_notes_to_file(notes)

                print("Заметка успешно удалена!")
                return

        print("Заметка с таким идентификатором не найдена!")
        
        
    #загрузка заметок из файла
    def load_notes_from_file(self):
        with open(self.filename, "r") as file:
            extension = self.filename.split(".")[-1]
            if extension == "json":
                notes = []
                for line in file:
                    note_data = json.loads(line)
                    note = Note(note_data["id"], note_data["title"], note_data["body"], note_data["date"])
                    notes.append(note)
            elif extension == "csv":
                reader = csv.reader(file, delimiter=";")
                next(reader) 
                notes = []
                for row in reader:
                    note = Note(row[0], row[1], row[2], row[3])
                    notes.append(note)
            else:
                raise ValueError("Unsupported file format!")
        return notes
    

    
    #сохранение заметок в файл
    def save_notes_to_file(self, notes):
        with open(self.filename, "w") as file:
            extension = self.filename.split(".")[-1]
            if extension == "json":
                for note in notes:
                    note_data = {
                        "id": note.id,
                        "title": note.title,
                        "body": note.body,
                        "date": note.date
                    }
                    json.dump(note_data, file)
                    file.write("\n")
            elif extension == "csv":
                writer = csv.writer(file, delimiter=";")
                writer.writerow(["id", "title", "body", "date"])
                for note in notes:
                    writer.writerow([note.id, note.title, note.body, note.date])
            else:
                raise ValueError("Unsupported file format!")


    #сохранение заметки в файл
    def save_note_to_file(self, note):
        notes = self.load_notes_from_file()
        notes.append(note)
        self.save_notes_to_file(notes)