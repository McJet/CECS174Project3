# Project3_Media

# Project Members: Jether Ysalina, Stephanie Lim, Andrea Dominguez, Lennox Scott, Michael Maalouf

"""
Jether Ysalina (Team Leader):
- Organized how group will work
- Set up base code for members to add to
- Fixed errors
- Made variables similar between the member's classes
- Fixed print issues
- Finalized code

Stephanie Lim:
- Tested Members class
- Contributed to Members class
- added comments

Andrea Dominguez:
- Worked on Media Class
- Contributed to Books subclass

Lennox Scott:
- Fixed on Media Class
- Contributed to Video subclass

Michael Maalouf:
- Contributed to Members class

"""


class Media:  # Superclass; Subclasses: Books and Videos
    # Keeps track of how many books and videos have been placed in Media
    numBooks = 0
    numVideos = 0
    bookList = []  # List of books that have been instantiated
    vidList = []  # List of videos that have been instantiated
    checkedOut = []  # List of items checked out of Media

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def displayStats(self):
        print("*" * 75)
        print("Record of Library:")
        print("Total number of books: {}".format(Media.numBooks))
        print("Total number of books checked out: {}".format())
        print("Total number of videos: {}".format(Media.numVideos))
        print("Total number of videos checked out: {}".format())
        print("Total number of members: {}".format(Members.num_members))


class Books(Media):  # Subclass of Media
    # initializes Books instance with attribute of Books
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.numPages = num_pages
        Media.numBooks += 1
        Media.bookList.append(self)

    # Prints the book details using print
    def __repr__(self):
        return "Book-->{} page book {} written by {}".format(self.numPages, self.title, self.author)


class Videos(Media):  # Subclass of Media
    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self.runTime = run_time
        Media.numVideos += 1
        Media.vidList.append(self)

    def __repr__(self):
        return "Video-->{} mins video {} created by {}".format(self.runTime, self.title, self.publisher)


class Members:  # Separate class
    memberList = []  # List of members' names
    num_members = 0  # tracks the number of members

    def __init__(self, name):  # define attributes
        self.name = name  # attribute for member name
        self.itemCheckOutList = []
        self.numItemChecked = 0  # initialize the number of items checked out
        Members.num_members += 1
        Members.memberList.append(self)

    def checkOut(self, a_media):
        if a_media in Media.vidList or a_media in Media.bookList:
            if self.numItemChecked >= 2:  # create limit to num items checked out (2)
                print("{} reached the maximum number(2) of borrowed items, so can't check out: {}".format(self, a_media.__repr__()))

            elif a_media in Media.checkedOut:
                # for loop used to find the name of the person who checked out the item
                member = ""
                for name in Members.memberList:
                    for item in name.itemCheckOutList:
                        if item == a_media:
                            member = name
                print("Sorry {}, {} is not available, checked out by {}".format(self, a_media, member))

            else:
                self.numItemChecked += 1  # increment for number of books checked out
                self.itemCheckOutList.append(a_media)  # add to check out list for member
                Media.checkedOut.append(a_media)  # add to check out list for media
                print("{} has checked out: {}".format(self, a_media))  # output the member and media info

    def checkIn(self, a_media):
        self.itemCheckOutList.remove(a_media)
        Media.checkedOut.remove(a_media)
        self.numItemChecked -= 1  # decrement for number of books checked out
        print("{} checked in: {}".format(self, a_media.__repr__()))  # output the member and media info

    def printCheckedOutItems(self):
        print('Items checked out by {}:'.format(self))
        for item in self.itemCheckOutList:  # print each media in check out list
            print(item)

    def __repr__(self):
        return self.name

video1 = Videos("Avengers", "Stan Lee", "Marvel", 143)
video2 = Videos("Jurassic Park", "Spielberg", "Penguin", 124)
video3 = Videos("The Man From U.N.C.L.E.", "Guy Fieri", "Lions", 156)
book1 = Books("Hunger Games", "Suzanne Collins", "Scholastic Corporation", 504)
book2 = Books("Book Thief", "James Bay", "SPeople", 374)
book3 = Books("Hunger Games", "Hasslehoff", "Pink", 236)


Joe = Members('Joe Smith')
Park = Members('Park Smith')

Joe.checkOut(book1)
Joe.checkOut(video1)
Joe.checkOut(video2)
Joe.checkOut(video3)
Joe.checkIn(book1)
Joe.printCheckedOutItems()
Park.checkOut(video2)
Park.checkOut(video1)

print(Media.displayStats())