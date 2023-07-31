#Create a dictionary of book titles and their respective authors, 
#write a Python program that allows users to search for books by entering either 
#the title or author's name.

def searching(dict1,search_book):
    books =[]
    for title,author in dict1.items():
        if search_book.lower() in title.lower() or search_book.lower() in author.lower():
            books.append((title,author))
    return books



dict1 ={
'b1':'a1','b2':'a2','b3':'a3','b4':'a4'
}

while True:
    Select_option=input('Enter "title" to search book by title or Enter "author" to search book by author')


    if Select_option.lower() == "exit":
        print("Exit")
        break
    elif Select_option.lower() not in ['title','author']:
        print('Invalid Option Selction by you please select again..')
        continue
    search_book = input("enter you search query: ")

    if Select_option.lower == 'title':
        result = searching(dict1,search_book)
    else:
        result = searching({x:y for x ,y in dict1.items()},search_book)

    if result:
        for title,author in result:
            print(f"{title} by {author}")
    else:
        print("No matching book is found")

