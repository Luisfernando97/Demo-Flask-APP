
# Demo Flask app

This project is a simple demonstration of my workflow utilizing Python in the backend using Flask is used with SQLAlchemy and PostgreSQL.

Docker is utilzed to containerize the application and database.

# Requirements

`docker` and `docker-compose` are required to run this script

# Setup

Clone this repository

`git clone https://github.com/Luisfernando97/Demo-Flask-APP`

Build and start the containers

`docker-compose up`

Now, we have to perform a database migration, this takes our model defined in `server/model.py` and creates the tables in the database, for that we need to access the backend shell

`docker-compose exec demo-be bash`

Run the following commands:

`flask --app backend db init` 

`flask --app backend db migrate`

`flask --app backend db upgrade`

# Usage

This script have two endpoints

POST /users/create

Expects a JSON with the keys 'name' and 'email', the informed data will be stored on the database

GET /users/list

Returns a JSON with 'name', 'email' and 'id' of all users stored in the database

# Demo

For demonstration purposes we can use `curl` but other REST clients such as Postman can be also used.

Create a user with:

`curl -X POST --json '{"name":"Luis Martins", "email":"luis.martins@mail.example"}' http://localhost:5002/users/create`

List all users with:

`curl -X GET http://localhost:5002/users/list`