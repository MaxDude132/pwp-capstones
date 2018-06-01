class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User " + self.name + " now has email: "+self.email)

    def get_average_rating(self):
        avg = 0
        rated_books = 0
        for value in self.books.values():
            if value:
                avg += value
                rated_books += 1
        avg = avg/rated_books
        return avg

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def __repr__(self):
        return self.name + ", email: "+self.email+", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("Book " + self.title + " now has an ISBN of "+str(self.isbn))

    def add_rating(self, rating):
        if rating and rating > 0 and rating <=4:
            self.ratings.append(rating)

    def get_average_rating(self):
        avg = 0
        for rating in self.ratings:
            avg += rating
        avg = avg/len(self.ratings)
        return avg

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject

class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_book = Fiction(title, author, isbn)
        return new_book

    def create_non_fiction(self, title, subject, level, isbn):
        new_book = Non_Fiction(title, subject, level, isbn)
        return new_book

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email " + email)

    def get_most_read_book(self):
        max_reads = float("-inf")
        most_read = None

        for book in self.books:
            num_reads = self.books[book]
            if num_reads > max_reads:
                max_reads = num_reads
                most_read = book

        return most_read

    def highest_rated_book(self):
        highest_rating = float("-inf")
        best_book = None

        for book in self.books:
            avg = book.get_average_rating()
            if avg > highest_rating:
                highest_rating = avg
                best_book = book

        return best_book


    def most_positive_user(self):
        highest_rating = float("-inf")
        nicest_user = None

        for user in self.users.values():
            avg = user.get_average_rating()
            if avg > highest_rating:
                highest_rating = avg
                nicest_user = user

        return nicest_user

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_user_average_rating(self, email):
        user = self.users.get(email, None)
        if user:
            return user.get_average_rating()
        return "No such user"