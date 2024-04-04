from backend import app
from server.services import main_service as ms

from flask import request

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/list', methods = ['GET'])
def get_all_users():
    return ms.get_all_users()

@app.route('/users/create', methods = ['POST'])
def create_user():

    body = request.get_json()
    first_name = body['name']
    email = body['email']
    
    return ms.create_user(first_name, email)