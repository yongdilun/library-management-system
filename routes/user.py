from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response, flash
from app import DAO
from Misc.functions import *

from Controllers.UserManager import UserManager

user_view = Blueprint('user_routes', __name__, template_folder='/templates')

user_manager = UserManager(DAO)

@user_view.route('/', methods=['GET'])
def home():
	g.bg = 1

	user_manager.user.set_session(session, g)
	print(g.user)

	return render_template('home.html', g=g)


@user_view.route('/signin', methods=['GET', 'POST'])
@user_manager.user.redirect_if_login
def signin():
	if request.method == 'POST':
		_form = request.form
		email = clean_text(_form["email"])
		password = clean_text(_form["password"])

		if len(email)<1 or len(password)<1:
			return render_template('signin.html', error="Email and password are required")

		d = user_manager.signin(email, password)

		if d and len(d)>0:
			session['user'] = int(d['id'])

			return redirect("/")

		return render_template('signin.html', error="Email or password incorrect")


	return render_template('signin.html')


@user_view.route('/signup', methods=['GET', 'POST'])
@user_manager.user.redirect_if_login
def signup():
	if request.method == 'POST':
		name = clean_text(request.form.get('name'))
		email = clean_text(request.form.get('email'))
		password = clean_text(request.form.get('password'))

		if len(name) < 1 or len(email)<1 or len(password)<1:
			return render_template('signup.html', error="All fields are required")
		if not valid_email(email):
			return render_template('signup.html', error="Please enter a valid email address")
		if len(password) < 6:
			return render_template('signup.html', error="Password must be at least 6 characters")

		new_user = user_manager.signup(name, email, password)

		if new_user == "already_exists":
			return render_template('signup.html', error="User already exists with this email")


		return render_template('signup.html', msg = "You've been registered!")


	return render_template('signup.html')


@user_view.route('/signout/', methods=['GET'])
@user_manager.user.login_required
def signout():
	user_manager.signout()

	return redirect("/", code=302)

@user_view.route('/user/', methods=['GET'])
@user_manager.user.login_required
def show_user(id=None):
	user_manager.user.set_session(session, g)
	
	if id is None:
		id = int(user_manager.user.uid())

	d = user_manager.get(id)
	mybooks = user_manager.getBooksList(id)

	return render_template("profile.html", user=d, books=mybooks, g=g)

@user_view.route('/user', methods=['POST'])
@user_manager.user.login_required
def update():
	user_manager.user.set_session(session, g)
	
	_form = request.form
	name = clean_text(_form["name"])
	email = clean_text(_form["email"])
	password = clean_text(_form["password"])
	bio = clean_text(_form["bio"])

	if len(name) < 1:
		d = user_manager.get(user_manager.user.uid())
		mybooks = user_manager.getBooksList(user_manager.user.uid())
		return render_template("profile.html", user=d, books=mybooks, g=g, error="Name is required")
	if not valid_email(email):
		d = user_manager.get(user_manager.user.uid())
		mybooks = user_manager.getBooksList(user_manager.user.uid())
		return render_template("profile.html", user=d, books=mybooks, g=g, error="Please enter a valid email address")
	if password and len(password) < 6:
		d = user_manager.get(user_manager.user.uid())
		mybooks = user_manager.getBooksList(user_manager.user.uid())
		return render_template("profile.html", user=d, books=mybooks, g=g, error="Password must be at least 6 characters")

	user_manager.update(name, email, password, bio, user_manager.user.uid())

	flash('Your info has been updated!')
	return redirect("/user/")
