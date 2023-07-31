# program 8 : 
    
books_with_authors = {
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'To Kill a Mockingbird': 'Harper Lee',
    '1984': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen',
    'Harry Potter and the Sorcerer\'s Stone': 'J.K. Rowling',
    'The Lord of the Rings': 'J.R.R. Tolkien',
    'Brave New World': 'Aldous Huxley',
    'The Catcher in the Rye': 'J.D. Salinger',
    'The Hobbit': 'J.R.R. Tolkien',
    'The Da Vinci Code': 'Dan Brown'
}



target = input("Enter the title or author : ")

for (x, y) in books_with_authors.items() :
    if x.__contains__(target) or y.__contains__(target) :
        print(x, "author - ", y)
    