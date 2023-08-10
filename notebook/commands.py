import read_file as rf
import save_file as sf
import Note as N

def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = N.Note(title=title, body=body)
    array_notes = rf.read_file()
    for i in array_notes:
        if N.Note.get_id(note) == N.Note.get_id(i):
            N.Note.set_id(note)
    array_notes.append(note)
    sf.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")


def show(txt):
    array_notes = rf.read_file()

    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for i in array_notes:
                print(N.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", N.Note.get_id(i))
            id = input("\nВведите id заметки: ")
            flag = True
            for i in array_notes:
                if id == N.Note.get_id(i):
                    print(N.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(N.Note.get_date(i))
                if date == date_note[:10]:
                    print(N.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой!")


def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = rf.read_file()
    flag = False

    for i in array_notes:
        if id == N.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        sf.write_file(array_notes, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = rf.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == N.Note.get_id(i):
            i.title = input("измените  заголовок:\n")
            i.body = input("измените  описание:\n")
            N.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        sf.write_file(array_notes_new, 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("нет такого id")