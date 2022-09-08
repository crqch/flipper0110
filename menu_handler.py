# Makes a list of all the functions that are then returned with correct callbacks to main

menu_object = {}


def get_menu():
    return menu_object


def add_to_menu(name, callback):
    menu_object[len(menu_object) + 1] = [name, callback]
