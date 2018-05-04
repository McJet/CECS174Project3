# Project3_Media

# Project Members: Jether Ysalina, Stephanie Lim, Andrea Dominguez, Lennox Scott, Michael Maalouf

"""
Jether Ysalina (Team Leader):
- Organized how group will work
- Set up base code for members to add to
- Worked on Media Class

Stephanie Lim:
- Help with member class by adding attributes and skeleton methods

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
        self.num_videos = 0

class Books(Media): # Subclass of Media
    def __init__(self, title, author, publisher,num_pages):
        super().__init__(title, author, publisher) # inherit attributes from Media
        self.num_pages = num_pages # add attribute for number of pages
        self.num_books += 1 # increment to keep track of number of books
    def __repr__(self): # return information of the class books
        return "Book--> {} page book {} written by {}".format(self.num_pages,self.title, self.author)

class Videos(Media): #Subclass of Media
    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher) # inherit attributes from Media
        self.run_time = run_time # add attribute for run time
        self.num_videos += 1 # increment to keep track of number of videos
    def __repr__(self): # return information of the class video
        return "Video --> {} min video {} created by {}".format(self.run_time,self.title, self.author)


class Members: # Separate class
    def __init__(self,name): # define attributes
        self.name = name # attribute for member name
        self.bookCheckOutList = []
        self.num_members = 0 # initialize the number of members
        self.list_members = []
        self.num_books_checked = 0 # initialize the number of books checked out

    def addMembers(self):
        self.num_members += 1 # increment to keep track of number of members

        #### FIXME: Have to figure out how to list all the members ####

    def checkOut(self,a_media):

        #### FIXME: Have to figure out how to prevent checking out the same book ####

        if self.num_books_checked > 1: # create limit to num books checked out (2)
            print("{} reached the maximum number(2) of borrowed items, so can't check out:{}".format(self.name, a_media))
        else:
            self.num_books_checked += 1 # increment for number of books checked out
            print("{} has checked out: {}".format(self.name, a_media)) # output the member and media info

    def checkIn(self, a_media):

        self.num_books_checked -= 1 # decrement for number of books checked out
        print("{} checked in: {}".format(self.name, a_media)) # output the member and media info


a_book1 = Videos("Hello","Steph Lim","Penguin",100)
a_book2 = Books("Bye","Steph","Penguin",200 )
a_book3 = Videos("Hi","Steph Lim","Penguin",300)
a_book4 = Videos("Sup","Steph Lim","Penguin",300)
student = Members('Lim')
student.checkOut(a_book1)
student.checkOut(a_book2)
student.checkOut(a_book3)
student.checkOut(a_book4)
student2 = Members('Park')