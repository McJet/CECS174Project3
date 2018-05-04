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
        self.num_books = 0
        self.num_vids = 0

class Books(Media): # Subclass of Media
    # intializes Books instance with atribute of Books
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.num_pages = num_pages
        self.num_books += 1
    # Prints the book details using print
    def __repr__(self):
        return "Book--> {} page book {} written by {}".format(self.pages, self.title, self.author)

class Videos(Media): #Subclass of Media
    def _init__(self, title, author, publisher, runTime):
        super().__init__(title, author, publisher)
        self.runTime = runTime



class Members: # Separate class
    pass