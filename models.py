from config import db

class Object(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.str(64), index=True, unique=True)

	def __repr__(self):
		return self.name

