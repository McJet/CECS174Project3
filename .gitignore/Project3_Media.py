# Project3_Media

# Project Members: Jether Ysalina, Stephanie Lim, Andrea Dominguez, Lennox Scott, Michael Maalouf

"""
Jether Ysalina (Team Leader):
- Organized how group will work
- Set up base code for members to add to
- Combined all the members code into one
- Contributed to Media, Book, Videos, and Members classes
- Fixed errors
- Fixed variables
- Fixed print issues
- Finalized code

Stephanie Lim:
- Heavily contributed to Members class
- Tested Members class
- Added comments

Andrea Dominguez:
- Made Books subclass
- Contributed to class implementation
- Added comments

Lennox Scott:
- Made Video subclass
- Contributed to Media displayStats() method
- Tested finalized version of code

Michael Maalouf:
- Contributed to Members class
- Added comments

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
        vid_num = 0
        book_num = 0
        # for loop used to find amount of book and videos checked out
        for item in self.checkedOut:
            for book in self.bookList:
                if item == book:
                    book_num += 1
            for video in self.vidList:
                if item == video:
                    vid_num += 1
        print('\n' + ("*" * 75) + '\n')  # asterisk divider
        print("Record of Library:")
        print("Total number of books= {}".format(self.numBooks))
        print("Total number of books checked out= {}".format(book_num))
        print("Total number of videos= {}".format(self.numVideos))
        print("Total number of videos checked out= {}".format(vid_num))
        print("Total number of members= {}".format(Members.num_members))
        print('\n' + ("*" * 75) + '\n')  # asterisk divider
        print("The following items are checked out of the library:")
        # prints every checked out item in the checkedOut list
        for item in Media.checkedOut:
            print(item)


class Books(Media):  # Subclass of Media
    # initializes Books instance with attribute of Books
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.numPages = num_pages
        Media.numBooks += 1
        Media.bookList.append(self)

    # Prints the book details using print
    def __repr__(self):
        return "Book-->{} written by {}".format(self.title, self.author)


class Videos(Media):  # Subclass of Media
    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self.runTime = run_time
        Media.numVideos += 1
        Media.vidList.append(self)

    def __repr__(self):
        return "Video-->{} mins video {} created by {}".format(self.runTime, self.title, self.author)


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
        # checks if a_media exists in Media.vidList or Media.bookList
        if a_media in Media.vidList or a_media in Media.bookList:
            if self.numItemChecked >= 2:  # checks if the member has checked out two or more items
                print("{} reached the maximum number(2) of borrowed items, so can't check out: {}".format(self, a_media.__repr__()))

            # checks if the media item is checked out or not
            elif a_media in Media.checkedOut:
                # for loop used to find the name of the person who checked out the item
                member = ""
                for name in self.memberList:
                    for item in name.itemCheckOutList:
                        if item == a_media:
                            member = name
                print("Sorry {}, {} is not available, checked out by {}".format(self, a_media, member))

            else:  # checks item out to the member
                self.numItemChecked += 1  # increment for number of books checked out
                self.itemCheckOutList.append(a_media)  # add to check out list for member
                Media.checkedOut.append(a_media)  # add to check out list for media
                print("{} has checked out: {}".format(self, a_media))  # output the member and media info

    def checkIn(self, a_media):  # checks item in to be put back to media
        if a_media in self.itemCheckOutList:
            self.itemCheckOutList.remove(a_media)
            Media.checkedOut.remove(a_media)
            self.numItemChecked -= 1  # decrement for number of books checked out
            print("{} checked in: {}".format(self, a_media.__repr__()))  # output the member and media info
        else:
            print("{} does not have {}".format(self, a_media.__repr__()))

    def printCheckedOutItems(self):
        print('Items checked out by {}:'.format(self))
        for item in self.itemCheckOutList:  # print each media in check out list
            print(" " * 3 + str(item))

    def __repr__(self):
        return self.name


# Test code

# creates instances for books
video1 = Videos("Avengers", "Stan Lee", "Marvel", 143)
video2 = Videos("Jurassic Park", "Spielberg", "Penguin", 124)
video3 = Videos("The Man From U.N.C.L.E.", "Guy Fieri", "Lions", 156)

# creates instances for videos
book1 = Books("Hunger Games", "Suzanne Collins", "Scholastic Corporation", 504)
book2 = Books("Book Thief", "James Bay", "SPeople", 374)
book3 = Books("Hunger Games", "Hasslehoff", "Pink", 236)

# creates two members
Joe = Members('Joe Smith')
Ron = Members('Ron Swanson')

Joe.checkOut(book1)
Joe.checkOut(video1)
Joe.checkOut(video2)  # attempts to check out a third item
Joe.printCheckedOutItems()
Ron.checkOut(video2)
Ron.checkOut(video1)  # attempts to check out an already checked out item
Joe.checkIn(video1)  # Joe returns item,
Ron.checkOut(video1)  # so Ron can check out that item
Ron.checkIn(book3)  # tries to return an item that he does not have
Joe.printCheckedOutItems()
Ron.printCheckedOutItems()
Media.displayStats(Media)
