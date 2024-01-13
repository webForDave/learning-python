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

     reading_list.append({
        "title": title,
        "author": author,
        "year": year
      })


def show_book() :
        for book in reading_list:
            print(f"{book['title']}, by {book['author']} ({book['year']})")

while selected_option != 'q' :

    if selected_option == 'a' :
        add_book()

    elif selected_option == 'l' :
        show_book()

    else : 
        print(f'Sorry, {selected_option} isn\'t a valid option')

    selected_option = input(menu_prompt).strip().lower()
