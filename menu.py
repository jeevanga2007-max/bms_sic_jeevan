def get_menu(choice):
    menu={
        1:insert,
        2:delete,
        3:update,
        4:display,
        5:exit
    }
    return menu[choice]
    

def run_menu():
    while True:
