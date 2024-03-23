#Task 1 D:Rewrite the entire Task 1 C using Data frames instead of lists.
#Use Pandas 

import pandas as pd


# Dictionary
bookD=({"book_Id":[2234],
                   "title":[ "The big House"],
                     "author": [" Sizelephi"],
                     "status": ["NOT AVAILABLE"]
                     })

dfB = pd.DataFrame(bookD)   
print("Data Frame for books: ", dfB)

memberD=({"member_id": [3444],
                     "name" : ["Msi"],
                     "borrowed_books":[[]]
                     })
dfM = pd.DataFrame(memberD)
print('Data Frame for members:',dfM)

