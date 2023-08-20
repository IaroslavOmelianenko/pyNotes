
from note_service import NoteService

#запуск приложения с управлением из консоли
if __name__ == "__main__":
    filename = "notes.json"
    service = NoteService(filename)

    while True:
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            service.create_note()
        elif choice == "2":
            service.read_notes()
        elif choice == "3":
            service.edit_note()
        elif choice == "4":
            service.delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный номер команды!")