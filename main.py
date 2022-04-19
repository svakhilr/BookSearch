from books import Book
from data import books_data
from search import Search_Engine

Books=[]

for book in books_data:
    # creating books objects and appending to the book list
    book_title=book['title']
    book_author=book['author']
    book_copies=book['copies']
    book_price=book["price"]
    author_loyalty=book["loyalty"]
    author_royalty=book["royalty"]
    book_obj=Book(title=book_title,author=book_author,copies=book_copies,royalty=author_royalty,loyalty=author_loyalty,price=book_price)
    Books.append(book_obj)


book_search=Search_Engine(Books) # creating a search engine object which consist of a list of book object


searching=True
while searching:

    print("--------welcome to bookshop--------")
    search_title=input('Enter the title: ')
    search_author=input('Enter the author: ')
    search_success=book_search.search(title=search_title,author=search_author)

    if search_success !=0:
        print('BOOK NOT FOUND')

    continue_search=input("Do you want to continue search yes or no ")

    if continue_search.lower() == 'yes':
        searching=True
    else:
        searching=False




