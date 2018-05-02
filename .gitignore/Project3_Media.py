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
    pass

class Videos(Media): #Subclass of Media
    pass

class Members: # Separate class
    def __init__(self,name):
        self.name = name
        self.bookCheckOutList = []
        self.num_members = 0
        self.list_members = []
        self.num_books_checked = 0
    def addMembers(self):
        self.num_members += 1

    def checkOut(self,a_media):

        self.num_books_checked += 1
        print("{} has checked out: {}".format(self.name, a_media))

    def checkIn(self, a_media):

        self.num_books_checked -= 1
        print("{} checked in: {}".format(self.name, a_media))