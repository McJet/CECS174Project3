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
- Contributed to Books subclass

Lennox Scott:
- Contributed to Video subclass

Michael Maalouf:
-

"""

class Media: # Superclass; Subclasses: Books and Videos
    # Keeps track of how many books and videos have been placed in Media
    numBooks = 0
    numVideos = 0

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def displayStats(self):
        print("FixMe")

class Books(Media): # Subclass of Media
    # initializes Books instance with attribute of Books
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.numPages = num_pages
        Media.numBooks += 1

    # Prints the book details using print
    def __repr__(self):
        return "Book--> {} page book {} written by {}".format(self.numPages, self.title, self.author)

class Videos(Media): #Subclass of Media
    # List of videos that have been instantiated
    vidList = []

    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self.runTime = run_time
        Media.numVideos += 1
        self.vidList.append("{} {} {} {}".format(self.title, self.author, self.publisher, self.runTime))

    def __repr__(self):
        return "Video-->{} minute video {} created by {}".format(self.runTime, self.title, self.publisher)

class Members: # Separate class
    pass

# Videos subclass test
video1 = Videos("Avengers", "Stan Lee", "Marvel", 143)
print(Videos.vidList)
print(Media.numVideos)
print(video1.__repr__())

# Books subclass test
book1 = Books("Hunger Games", "Suzanne Collins", "Scholastic Corporation", 374)
print(Media.numBooks)
print(book1.__repr__())