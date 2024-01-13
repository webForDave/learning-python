reading_list = []

menu_prompt = """Please enter one of the following options :

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

Please what would you like to do? """

selected_option = input(menu_prompt).strip().lower()

def add_book() :
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    new_book = {
        "title": title,
        "author": author,
        "year": year
    }

    reading_list.append(new_book)


def show_book() :
    print('Displaying...')

while selected_option != 'q' :

    if selected_option == 'a' :
        add_book()

    elif selected_option == 'l' :
        show_book()

    else : 
        print(f'Sorry, {selected_option} isn\'t a valid option')

    selected_option = input(menu_prompt).strip().lower()
