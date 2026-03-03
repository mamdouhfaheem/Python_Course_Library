
# book , title, no_of_pages, author

from book_handler import get_book_info, display_all_books

def start_app():
    while True:
        choice = input("Please enter n for new l for list all, e for exit")
        if choice == "n":
            print("--- new book ")
            get_book_info()
        elif choice == "l":
            print("--- list all books ")
            display_all_books()
        elif choice == "e":
            print("--- exit")
            exit()
        else:
            print("please enter valid choice")

if __name__ == "__main__":
    start_app()