class Search_Engine:
    #class for search engine

    def __init__(self,library):
        self.books_library = library #library is list of  book objects


    def dislay(self,book_obj):
        print("---------------BOOK DETAILS-------------")
        print(f"BOOK TITLE :  {book_obj.title}")
        print(F"AUTHOR     : {book_obj.author}")
        print(f"AVAILABLE COPIES : {book_obj.copies}")
        print(f"PRICE  : {book_obj.price}  ")
        print("-----------------------------------------")
        copies=int(input("ENTER THE REQUIRED NUMBER OF COPIES "))
        print(f"Total price {book_obj.price*copies} Rupees")
        book_obj.copies-=copies
        book_obj.sales+=1

        print(f"THANK YOU FOR PURCHASING VISIT AGAIN")
        #updadting author loyalty and royalty

        book_obj.loyalty=(10/100)*book_obj.price
        if book_obj.sales > 2:
            book_obj.royalty="GOLD"

        elif book_obj.sales>3:
            book_obj.royaty="platinum"



    def search(self,title,author):
        book_found=False

        for book in  self.books_library:

            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                self.dislay(book)
                book_found=True

        if book_found:
            return 0














