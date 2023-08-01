books = {
    "Godan": "Munshi Premchand",
    "Madhushala": "Harivansh Rai Bachchan",
    "Rag Darbari": "Shrilal Shukla",
    "Krishna": "Munshi Premchand",
    "Nirmala": "Munshi Premchand",
    "Virasat": "Bhagwati Charan Verma"
}

n = input("Enter the title or author: ")
b=0

for x,y in books.items():
    if x==n or y==n:
        print("The book is:", x, " and author is ",y)
        b = 1

if b==0:
    print("Not available")