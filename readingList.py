reading_list = []

menu_prompt = """Please enter one of the following options :

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

Please what would you like to do?"""

selected_option = input(menu_prompt).strip().lower()

while selected_option != 'q' :
    if selected_option == 'a' :
        print('Adding...')

    elif selected_option == 'l' :
        print('Displaying...')

    else : 
        print(f'Sorry, {selected_option} isn\'t a valid option')

    selected_option = input(menu_prompt).strip().lower()
