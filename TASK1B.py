# Tak1 B Rewrite the entire task 1 and task 1B without using parameters and arguments in your functions
#Initialize two data structures to keep track of books and members both represented as lists
books = []
members = []

#The system features two functions (You must create these functions): add_book and add_member.
#The add_book
#function takes three parameters (book_id, title, author, status) and appends a new book dictionary to 
#the books list.

def add_book():
    books.append({"book_Id": int(input("enter the book id")),
                   "title": input("enter the title"),
                     "author": input("enter the author"),
                     "status": "NOT AVAILABLE"})
    #The add_member function, on the other hand, requires two parameters (member_id, 
#name) and appends a new member dictionary to the members list
 #empty list for borrowed_books to track the IDs of books each member has borrowed.   
def add_member():
    members.append({"member_id": int(input("enter member id")),
                     "name":input("emter the name"),
                     "borrowed_books":[]})
    
"""Task 1 A:
Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a 
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. How would these 
additions reflect in the books and members lists, and what would the output look like if you printed 
both lists immediately after these additions?""
Hint: call the functions and write a print statement for them"""

#call the functions 
add_book()
add_member()

#write a print statement for them
print("books", books)
print("\nmembers", members)