#Task 1 C:Rewrite the entire task 1B without using functions

books = []
members = []


# Dictionary
bookD=({"book_Id": int(input("enter the book id")),
                   "title": input("enter the title"),
                     "author": input("enter the author"),
                     "status": "NOT AVAILABLE"})
books.append(bookD)    


memberD=({"member_id": int(input("enter member id")),
                     "name":input("emter the name"),
                     "borrowed_books":[]})
members.append(memberD)


#write a print statement for them
print("books", books)
print("\nmembers", members)
