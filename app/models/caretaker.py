from app import db

class Caretaker(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    cats = db.relationship("Cat", back_populates="caretaker") 