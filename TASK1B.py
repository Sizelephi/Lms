# Tak1 B Rewrite the entire task 1 and task 1B without using parameters and arguments in your functions

books = []
members = []



def add_book():
    books.append({"book_Id": int(input("enter the book id")),
                   "title": input("enter the title"),
                     "author": input("enter the author"),
                     "status": "NOT AVAILABLE"})
       
def add_member():
    members.append({"member_id": int(input("enter member id")),
                     "name":input("emter the name"),
                     "borrowed_books":[]})


#call the functions 
add_book()
add_member()

#write a print statement for them
print("books", books)
print("\nmembers", members) 