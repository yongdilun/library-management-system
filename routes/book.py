from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO
from Misc.functions import clean_text

from Controllers.UserManager import UserManager
from Controllers.BookManager import BookManager

book_view = Blueprint('book_routes', __name__, template_folder='/templates')

book_manager = BookManager(DAO)
user_manager = UserManager(DAO)

@book_view.route('/books/', defaults={'id': None})
@book_view.route('/books/<int:id>')
def home(id):
	user_manager.user.set_session(session, g)

	if id != None:
		try:
			b = book_manager.getBook(id)
		except Exception:
			return render_template("books.html", books=[], g=g, error="Database error while retrieving book details.")

		print('----------------------------')
		print(b)

		user_books={}
		if user_manager.user.isLoggedIn():
			reserved = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())
			user_books = reserved['user_books'].split(',') if reserved and reserved.get('user_books') else []
		
		if b and len(b) <1:
			return render_template('book_view.html', error="No book found!")

		return render_template("book_view.html", books=b, g=g, user_books=user_books)
	else:
		try:
			b = book_manager.list()
		except Exception:
			return render_template("books.html", books=[], g=g, error="Database error while retrieving books.")

		user_books=[]
		if user_manager.user.isLoggedIn():
			reserved_books = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())
			
			if reserved_books is not None:
				user_books = reserved_books['user_books'].split(',')
		
		print("---------------------------------------")
		print(user_books)

		if b and len(b) <1:
			return render_template('books.html', error="No books found!")
	
		return render_template("books.html", books=b, g=g, user_books=user_books)


	return render_template("books.html", books=b, g=g)


@book_view.route('/books/add/<id>', methods=['GET'])
@user_manager.user.login_required
def add(id):
	user_id = user_manager.user.uid()
	result = book_manager.reserve(user_id, id)

	b = book_manager.list()
	user_manager.user.set_session(session, g)

	messages = {
		"err_out": ("error", "This book is currently unavailable."),
		"err_duplicate": ("error", "You have already reserved this book."),
		"err_limit": ("error", "Reservation limit reached. Please return a book before reserving another."),
	}
	if result in messages:
		key, value = messages[result]
		return render_template("books.html", books=b, g=g, **{key: value})

	return render_template("books.html", msg="Book reserved successfully", books=b, g=g)


@book_view.route('/books/search', methods=['GET'])
def search():
	user_manager.user.set_session(session, g)

	if "keyword" not in request.args:
		return render_template("search.html")

	keyword = clean_text(request.args["keyword"])

	if len(keyword)<1:
		b = book_manager.list()
		return render_template("books.html", books=b, g=g, error="Please enter a search keyword.")
	if len(keyword)>50:
		b = book_manager.list()
		return render_template("books.html", books=b, g=g, error="Search keyword must not exceed 50 characters.")

	d=book_manager.search(keyword)

	if len(d) >0:
		return render_template("books.html", search=True, books=d, count=len(d), keyword=escape(keyword), g=g)

	return render_template('books.html', error="No books found!", keyword=escape(keyword))

