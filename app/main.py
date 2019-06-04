from flask import Blueprint

from .extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
  user_collection = mongo.db.users
  user_collection.insert({'name': 'Daniel', 'language': 'Python'})
  user_collection.insert({'name': 'Tiago', 'language': 'C'})
  return '<h1>User added</h1>'


@main.route('/find')
def find():
  user_collection = mongo.db.users
  user = user_collection.find_one({'name': 'Tiago'})
  return f'<h1>User: { user["name"] } Language: { user["language"] } </h1>'


@main.route('/update')
def update():
  user_collection = mongo.db.users
  user = user_collection.find_one({'name': 'Tiago'})
  user["language"] = 'Javascript'
  user_collection.save(user)
  return '<h1>User updated</h1>'


@main.route('/delete')
def delete():
  user_collection = mongo.db.users
  user = user_collection.find_one({'name': 'Tiago'})
  user_collection.remove(user)
  return '<h1>User removed</h1>'