from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO
from Misc.functions import *

from Controllers.AdminManager import AdminManager
from Controllers.BookManager import BookManager
from Controllers.UserManager import UserManager

admin_view = Blueprint('admin_routes', __name__, template_folder='../templates/admin/', url_prefix='/admin')

book_manager = BookManager(DAO)
user_manager = UserManager(DAO)
admin_manager = AdminManager(DAO)


@admin_view.route('/', methods=['GET'])
@admin_manager.admin.login_required
def home():
	admin_manager.admin.set_session(session, g)

	return render_template('admin/home.html', g=g)


@admin_view.route('/signin/', methods=['GET', 'POST'])
@admin_manager.admin.redirect_if_login
def signin():
	g.bg = 1
	
	if request.method == 'POST':
		_form = request.form
		email = clean_text(_form["email"])
		password = clean_text(_form["password"])

		if len(email)<1 or len(password)<1:
			return render_template('admin/signin.html', error="Email and password are required")

		d = admin_manager.signin(email, password)

		if d and len(d)>0:
			session['admin'] = int(d["id"])

			return redirect("/admin")

		return render_template('admin/signin.html', error="Email or password incorrect")

	return render_template('admin/signin.html')


@admin_view.route('/signout/', methods=['GET'])
@admin_manager.admin.login_required
def signout():
	admin_manager.signout()

	return redirect("/admin/", code=302)


@admin_view.route('/users/view/', methods=['GET'])
@admin_manager.admin.login_required
def users_view():
	admin_manager.admin.set_session(session, g)

	id = int(admin_manager.admin.uid())
	admin = admin_manager.get(id)
	myusers = admin_manager.getUsersList()

	return render_template('users.html', g=g, admin=admin, users=myusers)



@admin_view.route('/books/', methods=['GET'])
@admin_manager.admin.login_required
def books():
	admin_manager.admin.set_session(session, g)

	id = int(admin_manager.admin.uid())
	admin = admin_manager.get(id)
	mybooks = book_manager.list(availability=0)

	return render_template('books/views.html', g=g, books=mybooks, admin=admin, msg=request.args.get("msg"), error=request.args.get("error"))

@admin_view.route('/books/<int:id>')
@admin_manager.admin.login_required
def view_book(id):
	admin_manager.admin.set_session(session, g)

	if id != None:
		b = book_manager.getBook(id)
		users = user_manager.getUsersByBook(id)

		print('----------------------------')
		print(users)
		
		if b and len(b) <1:
			return render_template('books/book_view.html', error="No book found!")

		return render_template("books/book_view.html", books=b, books_owners=users, g=g)


@admin_view.route('/books/add', methods=['GET', 'POST'])
@admin_manager.admin.login_required
def book_add():
	admin_manager.admin.set_session(session, g)

	if request.method == 'POST':
		book, error = parse_book_form(request.form)
		if error:
			return render_template('books/add.html', g=g, error=error, book=request.form)

		existing = book_manager.search(book["name"], 0)
		if any(clean_text(item["name"]).lower() == book["name"].lower() for item in existing):
			return render_template('books/add.html', g=g, error="A book with this title already exists.", book=request.form)

		book_manager.add(book)
		return redirect('/admin/books/?msg=Book added successfully')

	return render_template('books/add.html', g=g, book={})


@admin_view.route('/books/edit/<int:id>', methods=['GET', 'POST'])
@admin_manager.admin.login_required
def book_edit(id):
	admin_manager.admin.set_session(session, g)

	if id != None:
		b = book_manager.getBook(id)

		if not b:
			return redirect('/admin/books/?error=No book found')

		if request.method == 'POST':
			book, error = parse_book_form(request.form)
			if error:
				return render_template("books/edit.html", book=b, g=g, error=error)
			book_manager.update(id, book)
			return redirect('/admin/books/?msg=Book updated successfully')

		return render_template("books/edit.html", book=b, g=g)
	
	return redirect('/books')

@admin_view.route('/books/delete/<int:id>', methods=['GET'])
@admin_manager.admin.login_required
def book_delete(id):
	admin_manager.admin.set_session(session, g)
	id = int(id)

	if id is not None:
		book = book_manager.getBook(id)
		if not book:
			return redirect('/admin/books/?error=Book does not exist')
		try:
			book_manager.delete(id)
		except Exception:
			books = book_manager.list(availability=0)
			return render_template('books/views.html', g=g, books=books, error="Delete error while removing book.")
	
	return redirect('/admin/books/?msg=Book deleted successfully')


@admin_view.route('/books/search', methods=['GET'])
def search():
	admin_manager.admin.set_session(session, g)

	if "keyword" not in request.args:
		return render_template("books/view.html")

	keyword = clean_text(request.args["keyword"])

	if len(keyword)<1:
		return redirect('/admin/books/?error=Please enter a search keyword')

	id = int(admin_manager.admin.uid())
	admin = admin_manager.get(id)

	d=book_manager.search(keyword, 0)

	if len(d) >0:
		return render_template("books/views.html", search=True, books=d, count=len(d), keyword=escape(keyword), g=g, admin=admin)

	return render_template('books/views.html', error="No books found!", keyword=escape(keyword), g=g, admin=admin)


def parse_book_form(form):
	title = clean_text(form.get("title"))
	description = clean_text(form.get("desc"))
	author = clean_text(form.get("author")) or "Unknown"
	edition = clean_text(form.get("edition")) or "1"
	qty_raw = clean_text(form.get("qty"))
	availability = 1 if form.get("available") or form.get("avaliable") else 0

	if not title:
		return None, "Title is required."
	if not description:
		return None, "Description is required."
	if not qty_raw.isdigit() or int(qty_raw) < 0:
		return None, "Quantity must be a positive number or zero."

	return {
		"name": title,
		"desc": description,
		"author": author,
		"edition": edition,
		"count": int(qty_raw),
		"availability": availability,
	}, None

