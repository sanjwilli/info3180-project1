from . import db

class UserProfile(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80))
	last_name = db.Column(db.String(80))
	userid = db.Column(db.Integer, unique=True)
	age = db.Column(db.Integer)
	biography = db.Column(db.String(255))
	gender = db.Column(db.String(80))
	username = db.Column(db.String(80), unique=True)
	date = db.Column(db.String(80))

	def __init__(self, first_name, last_name, userid, age, biography, gender, username, date):
		self.first_name = first_name
		self.last_name = last_name
		self.userid = userid
		self.age = age
		self.biography = biography
		self.gender = gender
		self.username = username
		self.date = date

	def get_id(self):
		try:
			return unicode(self.id) # python 2 support
		except NameError:
			return str(self.id) # python 3 support

	def __repr__(self):
		return '<User %r>' % (self.username)