from backend import db
from server.model import (
    User
)

def get_all_users():

    users = db.session.query(User).all()
    json = [ user.serialize() for user in users]

    return json

def create_user(first_name, email):

    user = User(first_name=first_name, email=email)
    db.session.add(user)
    db.session.commit()

    return user.serialize()