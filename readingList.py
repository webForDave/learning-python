reading_list = []

menu_prompt = """Please enter one of the following options :

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

Please what would you like to do?"""

selected_option = input(menu_prompt).strip().lower()

def add_book() :
    print('Adding...')

def show_book() :
    print('Displaying...')

while True :
    selected_option = input(menu_prompt).strip().lower()


    if selected_option == 'a' :
        add_book()

    elif selected_option == 'l' :
        show_book()

    else : 
        print(f'Sorry, {selected_option} isn\'t a valid option')

    selected_option = input(menu_prompt).strip().lower()
