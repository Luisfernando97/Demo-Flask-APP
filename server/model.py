import datetime
import uuid

from enum import Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import FetchedValue

from backend import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, first_name, email):

        self.first_name = first_name
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'email': self.email
        }
