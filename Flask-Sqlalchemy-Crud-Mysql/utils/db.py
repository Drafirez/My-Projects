from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Hola(db.Model):
    __tablename__ = 'Hola'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    