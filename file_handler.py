
"""
    book_title:author_name:no_of_pages

"""

# save data to the file
def save_book_info(book_info: str):
    try:
        file = open("books.txt","a")
        file.write(book_info)
        file.close()
        return True
    except Exception as e :
        return False


# get data from file
def get_all_books():
    book_info = []
    try:
        file = open("books.txt","r")
        book_info = file.readlines()
        file.close()
        return book_info
    except Exception as e :
        print("--- Error while getting all books ---")
        return book_info


def generate_id():
    """
        get value in counter.txt, +1
        save new value in counter.txt
        :return with new value
    :return:
    """
    id = 0
    try:
        with open("counter.txt","r") as f:
            id = f.read()
            id = int(id)
            id +=1
        with open("counter.txt","w") as fileObj :
            fileObj.write(str(id))

    except Exception as e :
        id = 0

    return id