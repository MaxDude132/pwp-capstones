class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}

	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address
		print("The email address has successfully been changed to {0}.".format(self.email))

	def __repr__(self):
		if len(self.books) < 2:
			return "User {user}, email: {email}, has read {n} book.".format(user=self.name, email=self.email, n=len(self.books))
		else:
			return "User {user}, email: {email}, has read {n} books.".format(user=self.name, email=self.email, n=len(self.books))

	def __eq__(self, other):
		return self.name == other.name and self.email == other.email

	def __ne__(self, other):
		return self.name != other.name and self.email != other.email

	def read_book(self, book, rating=None):
		self.books[book] = rating
		book.ratings.append(rating)

	def get_average_rating(self):
		total = 0
		i = 0
		for value in self.books.values():
			if value:
				total += value
				i += 1
		try:
			return total / i
		except ZeroDivisionError:
			return 0

class Book(object):
	def __init__(self, title, isbn, price):
		self.title = title
		self.isbn = isbn
		self.price = price
		self.ratings = []

	def get_title(self):
		return self.title

	def get_isbn(self):
		return self.isbn

	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print("The new ISBN is: {0}.".format(self.isbn))

	def add_rating(self, rating):
		if rating >= 0 and rating <= 4:
			self.rating.append(rating)
		else:
			print("Invaild Request")

	def __eq__(self, other_book):
		return self.title == other_book.title and self.isbn == other_book.isbn

	def __ne__(self, other_book):
		return self.title != other_book.title or self.isbn != other_book.isbn

	def get_average_rating(self):
		total = 0
		i = 0
		for value in self.ratings:
			if value:
				total += value
				i += 1
		try:
			return total / i
		except ZeroDivisionError:
			return 0

	def __repr__(self):
		return self.title

	def __hash__(self):
		return hash((self.title, self.isbn))

class Fiction(Book):
	def __init__(self, title, author, isbn, price):
		super().__init__(title, isbn, price)
		self.author = author
		self.ratings = []

	def get_author(self):
		return self.author

	def __repr__(self):
		return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn, price):
		super().__init__(title, isbn, price)
		self.subject = subject
		self.level = level
		self.ratings = []

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return "{title}, a {level} manual on {subject}.".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater():
	def __init__(self):
		self.users = {}
		self.books = {}
		self.isbns = {}

	def create_book(self, title, isbn, price):
		if isbn not in self.isbns.values():	
			new_book = Book(title, isbn, price)
			self.isbns[title] = isbn
			return new_book
		else:
			print("This ISBN code is already being used for the book {title}.".format(title=title))

	def create_novel(self, title, author, isbn, price):
		if isbn not in self.isbns.values():	
			new_novel = Fiction(title, author, isbn, price)
			self.isbns[title] = isbn
			return new_novel
		else:
			print("This ISBN code is already being used for the novel {title}.".format(title=title))

	def create_non_fiction(self, title, subject, level, isbn, price):
		if isbn not in self.isbns.values():	
			new_non_fonction = Non_Fiction(title, subject, level, isbn, price)
			self.isbns[title] = isbn
			return new_non_fonction
		else:
			print("This ISBN code is already being used for the non fiction book {title}.".format(title=title))

	def add_book_to_user(self, book, email, rating=None):
		user = self.users.get(email, None)
		if user:
			user.read_book(book, rating)
			if book not in self.books:
				self.books[book] = 1
			else:
				self.books[book] += 1
		else:
			print("No user with email {0}".format(email))

	def add_user(self, name, email, user_books=None):
		if email not in self.users:	
			if "@" in email and (".com" in email or ".edu" in email or ".org" in email):
				new_user = User(name, email)
				self.users[email] = new_user
				if user_books:
					for book in user_books:
						self.add_book_to_user(book, email)
			else:
				print("This email is not valid.")
		else:
			print("This email is already being used for user {name}.".format(name=name))

	def print_catalog(self):
		for key in self.books.keys():
			print(key)

	def print_users(self):
		for value in self.users.values():
			print(value)

	def most_read_book(self):
		read = 0
		book = ""
		for a, b in self.books.items():
			if b > read:
				read = b
				book = a
		if read < 2:
			return "{book}, read {read} time.".format(book=book, read=read)
		else:
			return "{book}, read {read} times.".format(book=book, read=read)

	def highest_rated_book(self):
		high = 0
		high_book = ""
		for book in self.books:
			if book.get_average_rating() > high:
				high = book.get_average_rating()
				high_book = book
		return "{book}, rated {high}.".format(book=high_book, high=high)

	def most_positive_user(self):
		high = 0
		high_user = ""
		for user in self.users.values():
			if user.get_average_rating() > high:
				high = user.get_average_rating()
				high_user = user
		return "{user}, with an average rating of {high}.".format(user=high_user.name, high=high)

	def most_expensive_book(self):
		high = 0
		high_book = ""
		for book in self.books:
			if book.price > high:
				high = book.price
				high_book = book
		return "{b}, which costs {price}$.".format(b=str(high_book), price=high)

	def get_n_most_read_books(self, n):
		choices = dict(self.books)
		read = 0
		book = ""
		serie = ""
		i = 0
		while n > 0:
			for key, value in choices.items():
				if value > read:
					read = value
					book = key
			try:
				del choices[book]
			except KeyError:
				return("Not enough books for the number that was input.")
				break	
			n -= 1
			i += 1
			serie += "{I}: {b}, read {num} times.".format(I=i, b=str(book), num=read)
			if n != 0:
				serie += "\n"
			book = ""
			read = 0
		else:
			return serie

	def get_n_most_positive_users(self, n):
		choices = dict(self.users)
		high = 0
		high_user = ""
		high_list = ""
		k = ""
		i = 0
		while n > 0:
			for key, user in choices.items():
				if user.get_average_rating() > high:
					high = user.get_average_rating()
					high_user = user
					k = key
			try:
				del choices[k]	
			except KeyError:
				return("Not enough users for the number that was input.")
				break	
			n -= 1
			i += 1
			high_list += "{I}: {user}, with an average rating of {high}.".format(I=i, user=str(high_user.name), high=high)
			if n != 0:
				high_list += "\n"
			high_user = ""
			high = 0
		else:
			return high_list

	def get_n_most_expensive_books(self, n):
		choices = dict(self.books)
		high = 0
		book = ""
		book_list = ""
		k = ""
		i = 0
		while n > 0:
			for key in choices.keys():
				if key.price > high:
					high = key.price
					book = key
			try:
				del choices[book]
			except KeyError:
				return("Not enough books for the number that was input.")
				break
			n -= 1
			i += 1
			book_list += "{I}: {b}, which costs {price}$.".format(I=i, b=str(book), price=high)
			if n != 0:
				book_list += "\n"
			book = ""
			high = 0
		else:
			return book_list

	def get_worth_of_user(self, user_email):
		u = self.users[user_email]
		total = 0
		for book in u.books.keys():
			total += book.price
		return "{name} has {p}$ worth of books in his account.".format(name=u.name, p=round(total, 2))

	def __repr__(self):
		u = ""
		for user in self.users.values():
			u += str(user)
			u += "\n"
		b = ""
		for book in self.books.keys():
			b += str(book)
			b += "\n"
		return "Users:\n{users}\nBooks:\n{books}".format(users=u, books=b)

	def __eq__(self, other):
		return self.users == other.users and self.books == other.books

	def __ne__(self, other):
		return self.users != other.users or self.books != other.books





