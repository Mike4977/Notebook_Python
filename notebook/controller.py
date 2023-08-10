import main_menu as ui

import commands as com


def start():
    work = True
    while work:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("ID")
        elif user_input == '3':
            com.show("date")
        elif user_input == '4':
            com.show("all")
            com.change_note()
        elif user_input == '5':
            com.add_note()
        elif user_input == '6':
            com.show("all")
            com.del_notes()
        elif user_input == '7':
            print("Работа с записной книжкой завершена")
            work = False
