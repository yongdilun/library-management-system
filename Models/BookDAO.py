class BookDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "books"

	def delete(self, id):
		q = self.db.query("DELETE FROM @table where id=%s", (id,))
		self.db.commit()

		return q

	def add(self, book):
		q = self.db.query(
			"INSERT INTO @table (name, `desc`, author, availability, edition, count) VALUES(%s, %s, %s, %s, %s, %s)",
			(book["name"], book["desc"], book["author"], book["availability"], book["edition"], book["count"]),
		)
		self.db.commit()
		return q

	def update(self, id, book):
		q = self.db.query(
			"UPDATE @table SET name=%s, `desc`=%s, author=%s, availability=%s, edition=%s, count=%s WHERE id=%s",
			(book["name"], book["desc"], book["author"], book["availability"], book["edition"], book["count"], id),
		)
		self.db.commit()
		return q

	def reserve(self, user_id, book_id):
		if self.has_reserved(user_id, book_id):
			return "err_duplicate"

		if self.getBooksCountByUser(user_id)[0]["books_count"] >= 5:
			return "err_limit"

		q = self.db.query("UPDATE @table set count=count-1 where id=%s AND count > 0", (book_id,))
		if q.rowcount < 1:
			self.db.rollback()
			return "err_out"

		try:
			inserted = self.db.query("INSERT INTO reserve (user_id, book_id) VALUES(%s, %s)", (user_id, book_id))
			self.db.commit()
			return inserted
		except Exception:
			self.db.rollback()
			return "err_duplicate"

	def getBooksByUser(self, user_id):
		q = self.db.query("select * from @table left join reserve on reserve.book_id = @table.id where reserve.user_id=%s", (user_id,))

		books = q.fetchall()

		print(books)
		return books

	def getBooksCountByUser(self, user_id):
		q = self.db.query("select count(reserve.book_id) as books_count from @table left join reserve on reserve.book_id = @table.id where reserve.user_id=%s", (user_id,))

		books = q.fetchall()

		print(books)
		return books

	def getBook(self, id):
		q = self.db.query("select * from @table where id=%s", (id,))

		book = q.fetchone()

		print(book)
		return book

	def available(self, id):
		book = self.getById(id)
		count = book['count']

		if count < 1:
			return False

		return True

	def getById(self, id):
		q = self.db.query("select * from @table where id=%s", (id,))

		book = q.fetchone()

		return book

	def list(self, availability=1):
		query="select * from @table"
		# Usually when no-admin user query for book
		if availability==1: query= query+"  WHERE availability=1"
		
		books = self.db.query(query)
		
		books = books.fetchall()


		return books

	def getReserverdBooksByUser(self, user_id):
		query="select concat(book_id,',') as user_books from reserve WHERE user_id=%s"
		
		books = self.db.query(query, (user_id,))
		
		books = books.fetchone()


		return books

	def search_book(self, name, availability=1):
		query="select * from @table where (name LIKE %s OR author LIKE %s)"
		params = [f"%{name}%", f"%{name}%"]

		# Usually when no-admin user query for book
		if availability==1: query= query+"  AND availability=1"

		q = self.db.query(query, tuple(params))
		books = q.fetchall()
		
		return books

	def has_reserved(self, user_id, book_id):
		q = self.db.query("SELECT id FROM reserve WHERE user_id=%s AND book_id=%s LIMIT 1", (user_id, book_id))
		return q.fetchone() is not None
