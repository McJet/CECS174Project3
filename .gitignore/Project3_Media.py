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
    def __init__(self, title, author, publisher, runTime):
        super().__init__(title, author, publisher)
        self.runTime = runTime



class Members: # Separate class
    pass