from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "pisnai"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class data(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column("name", db.String(100), nullable = False)
	classroom = db.Column("classroom", db.Integer, nullable = False)
	date_time = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

	def __init__(self, name, classroom):
		self.name = name
		self.classroom = classroom
db.create_all()
temp = data(name = "pisnai", classroom = "62113")
temp2 = data(name = "halosung", classroom = "62115")

db.session.add(temp)
db.session.add(temp2)
db.session.commit()
# or
# db.session.add_all([temp, temp2])
# db.session.commit()

for i in data.query.all():
    print(i.id, i.name, i.classroom, i.date_time)
    
    
flask_sqlalchemy.version_info()
