from bake import db
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
	"""Holds User data for session management"""
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), unique = True)
	pwdhash = db.Column(db.String(54))
	tasks = db.relationship('List', backref = 'person', lazy = 'dynamic')

	def __init__(self, email, password):
		self.email = email.lower()
		self.set_password(password)

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

	def __repr__(self):
		return '<User %r>' % (self.email)

class List(db.Model):
	"""Holds the lists generated by users"""
	id = db.Column(db.Integer, primary_key = True)
	task = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return self.task
		
