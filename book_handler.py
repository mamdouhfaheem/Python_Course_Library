import uuid
import tabulate

from demo.inputsModule import  ask_for_int, ask_for_name, ask_for_non_empty_string
from file_handler import save_book_info, generate_id, get_all_books

# book , title, no_of_pages, author

def get_book_info():
    author_name =ask_for_name("Please enter Author Name: ")
    no_of_pages = ask_for_int("Please enter Number of Pages: ")
    title = ask_for_non_empty_string("Please enter Book Title: ")
    # id = uuid.uuid4()
    id = generate_id()
    book_info = f"{id}:{title}:{author_name}:{no_of_pages}\n"
    saved = save_book_info(book_info)
    if saved:
        print("---New Book Added successfully---")
    else:
        print("-------- Error while adding Book --------")


def display_all_books():
    books = get_all_books()
    print(books)
    booklist= []
    for book in books:
        print(book, type(book))
        bookdata = book.strip("\n")
        bookdata = bookdata.split(":")
        print(bookdata)
        booklist.append(bookdata)


    # print(tabulate.tabulate(books))
    print(tabulate.tabulate(booklist, headers=["id", "title", "author", "pages"]))


    # print("--------Listing all books--------")
    # for book in books:
    #     book = book.strip("\n")
    #     book = book.split(":")
    #     # print(f"id={book[0]}, title={book[1]}, author={book[2]}, pages={book[3]}")

"""
    proj_id: : : user_id
"""

