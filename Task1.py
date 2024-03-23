
#Initialize two data structures to keep track of books and members both represented as lists
books = []
members = []

#The system features two functions (You must create these functions): add_book and add_member.
#The add_book
#function takes three parameters (book_id, title, author, status) and appends a new book dictionary to 
#the books list.

def add_book(book_id, title, author, status):
    books.append({"book_Id": book_id,
                   "title": title,
                     "author": author, 
                     "status": status})
    #The add_member function, on the other hand, requires two parameters (member_id, 
#name) and appends a new member dictionary to the members list
 #empty list for borrowed_books to track the IDs of books each member has borrowed.   
def add_members(member_id, name):
    members.append({"member_id": member_id,
                     "name":name,
                     "borrowed_books":[]})
    
"""Task 1 A:
Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a 
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. How would these 
additions reflect in the books and members lists, and what would the output look like if you printed 
both lists immediately after these additions?""
Hint: call the functions and write a print statement for them"""

#call the functions 
add_book(2024001,"python programmin", "Jacob Zuma" , "Available")
add_member(1,"Anelisa Maleka")

#write a print statement for them
print("books", books)
print("\nmembers", members)







    

