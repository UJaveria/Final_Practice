# Create a dictionary describing a book (title, author, year); update the year and add a new key
# "genre" .

book = {
    "title" : "Atomic Habits",
    "author": "James Clear",
    "year"  : "2018"
}
book.update({"year" : "2019"})
book.update({"genre": "self-help and personal development"})
print(book)