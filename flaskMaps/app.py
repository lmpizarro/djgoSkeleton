from flask import Flask, request
from flask import jsonify
from flask.ext import restful
from flask.ext.restful import Resource, Api

from flask import abort
from flask import make_response


from flask import render_template

from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
api = restful.Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username





@app.route('/')
def index():
    return render_template('index.html')


class HelloWorld(restful.Resource):
    def get(self):
        return {'name': 'silvina', 'surname':'saettone'}



todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/todo/<int:todo_id>')


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/todo/tasks', methods = ['GET'])
def get_tasks():
    return jsonify( { 'tasks': tasks } )



@app.route('/todo/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify( { 'task': task[0] } )


@app.route('/todo/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'task': task } ), 201





api.add_resource(HelloWorld, '/api/')

if __name__ == '__main__':
    app.run(debug=True)

