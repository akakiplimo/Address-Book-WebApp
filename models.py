"""Included in app.py (IGNORE)"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AddressBookModel(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    phone = db.Column(db.String())
    email = db.Column(db.String())
    address = db.Column(db.String())

    def __init__(self, first_name, last_name, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"{self.first_name}:{self.last_name}:{self.phone}:{self.email}:{self.address}"
    