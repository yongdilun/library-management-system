class UserDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "users"


	def list(self):
		users = self.db.query("select @table.id,@table.name,@table.email,@table.bio,@table.mob,@table.lock,@table.created_at,count(reserve.book_id) as books_owned from @table LEFT JOIN reserve ON reserve.user_id=@table.id GROUP BY reserve.user_id").fetchall()

		return users

	def getById(self, id):
		q = self.db.query("select * from @table where id=%s", (id,))

		user = q.fetchone()

		return user

	def getUsersByBook(self, book_id):
		q = self.db.query("select * from @table LEFT JOIN reserve ON reserve.user_id = @table.id WHERE reserve.book_id=%s", (book_id,))

		user = q.fetchall()

		return user

	def getByEmail(self, email):
		q = self.db.query("select * from @table where email=%s", (email,))

		user = q.fetchone()

		return user

	def add(self, user):
		name = user['name']
		email = user['email']
		password = user['password']

		q = self.db.query(
			"INSERT INTO @table (name, email, password,bio,mob,`lock`) VALUES(%s, %s, %s, '', '', 0)",
			(name, email, password),
		)
		self.db.commit()
		
		return q


	def update(self, user, _id):
		name = user['name']
		email = user['email']
		password = user['password']
		bio = user['bio']

		q = self.db.query(
			"UPDATE @table SET name=%s, email=%s, password=%s, bio=%s WHERE id=%s",
			(name, email, password, bio, _id),
		)
		self.db.commit()
		
		return q
