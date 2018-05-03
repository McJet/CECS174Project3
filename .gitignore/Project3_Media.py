# Project3_Media

# Project Members: Jether Ysalina, Stephanie Lim, Andrea Dominguez, Lennox Scott, Michael Maalouf

"""
Jether Ysalina (Team Leader):
- Organized how group will work
- Set up base code for members to add to
- Worked on Media Class

Stephanie Lim:
-

Andrea Dominguez:
-

Lennox Scott:
-

Michael Maalouf:
-

"""

class Media: # Superclass; Subclasses: Books and Videos
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

class Books(Media): # Subclass of Media
    pages = ''
    bookCount = 0
    checkedBook = 0
    # the dictionary bks is used to store all book activity
    bks = {}

    # intializes Books instance with atribute of Books
    def __init__(self, title, author, publisher, pages):
        super().__init__(title, author, publisher)
        self.pages = pages
        # key is for dictionary bks for book of title a
        key = title

        # bkInfo is the information of other attributes which are stored in bks
        bkInfo = 'Author: %s' % author + 'Publisher: %s' % publisher + 'No. Pages: %s' % pages
        Books.bks[key] = bkInfo
        # calculates number of books
        Books.bookCount += 1
        self.checkedBook = 0
        
    # Prints the book details using prin
    def __repr__(self):
        return 'Book name: %s, Book author: %s, Book publisher: %s, Book pages: %s' % (
        self.title(), self.author(), self.publisher(), self.pages)


class Videos(Media): #Subclass of Media
    def __init__(self, title, author, publisher, runTime):
        super().__init__(title, author, publisher)
        self.runTime = runTime

class Members: # Separate class
    pass