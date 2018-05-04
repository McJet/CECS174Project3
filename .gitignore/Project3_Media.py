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
    def __init__(self, name):  # define attributes
        self.name = name  # attribute for member name
        self.bookCheckOutList = []
        self.num_members = 0  # initialize the number of members
        self.list_members = []
        self.num_books_checked = 0  # initialize the number of books checked out

    def addMembers(self):
        self.num_members += 1  # increment to keep track of number of members

    def checkOut(self, a_media):
        self.bookCheckOutList.append(a_media)
        #### FIXME: Have to figure out how to prevent checking out the same book ####

        if self.num_books_checked > 1:  # create limit to num books checked out (2)
            print(
                "{} reached the maximum number(2) of borrowed items, so can't check out:{}".format(self.name, a_media))
        else:
            self.num_books_checked += 1  # increment for number of books checked out
            print("{} has checked out: {}".format(self.name, a_media))  # output the member and media info

    def printCheckedOutItems(self):  # shows all the checked out items
        print('*' * 40)
        print('The following items are checked out of the library:')
        for item in self.bookCheckOutList:
            print(item)

    def checkIn(self, a_media):

        self.num_books_checked -= 1  # decrement for number of books checked out
        print("{} checked in: {}".format(self.name, a_media))  # output the member and media info


a_book1 = Videos("Hello", "Steph Lim", "Penguin", 100)
a_book2 = Books("Bye", "Steph", "Penguin", 200)
a_book3 = Videos("Hi", "Steph Lim", "Penguin", 300)
a_book4 = Videos("Sup", "Steph Lim", "Penguin", 300)
student = Members('Lim')
student.checkOut(a_book1)
student.checkOut(a_book2)
student.checkOut(a_book3)
student.checkOut(a_book4)
student.printCheckedOutItems()
student2 = Members('Park')