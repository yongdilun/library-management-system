import os
from pathlib import Path

from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


def load_local_env():
	env_path = Path(__file__).resolve().parents[1] / ".env"
	if not env_path.exists():
		return

	for line in env_path.read_text(encoding="utf-8").splitlines():
		line = line.strip()
		if not line or line.startswith("#") or "=" not in line:
			continue
		key, value = line.split("=", 1)
		key = key.strip()
		value = value.strip().strip('"').strip("'")
		os.environ.setdefault(key, value)


load_local_env()


class DB(object):
	"""Initialize mysql database """
	host = os.getenv("MYSQL_DATABASE_HOST", "localhost")
	user = os.getenv("MYSQL_DATABASE_USER", "root")
	password = os.getenv("MYSQL_DATABASE_PASSWORD", "")
	db = os.getenv("MYSQL_DATABASE_DB", "lms")
	table = ""

	def __init__(self, app):
		app.config["MYSQL_DATABASE_HOST"] = self.host;
		app.config["MYSQL_DATABASE_USER"] = self.user;
		app.config["MYSQL_DATABASE_PASSWORD"] = self.password;
		app.config["MYSQL_DATABASE_DB"] = self.db;

		self.mysql = MySQL(app, cursorclass=DictCursor)

	def cur(self):
		return self.mysql.get_db().cursor()

	def query(self, q):
		h = self.cur()
	
		if (len(self.table)>0):
			q = q.replace("@table", self.table)

		h.execute(q)

		return h

	def commit(self):
		self.query("COMMIT;")
