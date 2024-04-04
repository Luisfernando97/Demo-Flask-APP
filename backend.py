from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@database/postgres",
    SQLALCHEMY_MAX_OVERFLOW = 3000,
    SQLALCHEMY_POOL_SIZE = 20000,
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   )

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server.controllers import main_controller