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
- Contributed to Video subclass

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
    # List of videos that have been instantiated
    vidList = []
    num_videos = 0

    def __init__(self, title, author, publisher, runTime):
        super().__init__(title, author, publisher)
        self.runTime = runTime
        Videos.num_videos += 1
        self.vidList.append("{} {} {} {}".format(self.title, self.author, self.publisher, self.runTime))

    def __repr__(self):
        return "Video-->{} minute video {} created by {}".format(self.runTime, self.title, self.publisher)

class Members: # Separate class
    pass

# Videos Class Test
video1 = Videos("Avengers", "Stan Lee", "Marvel", "96")
print(Videos.vidList)
print(Videos.num_videos)
print(video1.__repr__())