from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\akshita.kukreja\\Downloads\\sqlitestudio-3.1.1\\SQLiteStudio\\toDos.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120))
    done = db.Column(db.Boolean,default=False)

    def __init__(self, task,done):
        self.task = task
        self.done = done
    
class TodoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('task','id','done')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


@app.route("/todo", methods=["POST"])
def add_todo():
    #taskNew = request.json['task']
    #student = students(request.form['name'], request.form['city'],request.form['addr'], request.form['pin'])
    #print(request.json['data'])
    print(request.form['task'])
    task = request.form['task']
    #done = request.json['done']
    done = False
    new_task = Todo(task,done)
    obj={
    "task" : task,
    "done" : done
    }
    db.session.add(new_task)
    db.session.commit()
    return jsonify(obj)
    
@app.route("/todo", methods=["GET"])
def get_todo():
    all_tasks = Todo.query.all()   #id wise <Todo 1><Todo2>
    result = todos_schema.dump(all_tasks)   #dump the ids of database in text format
    print(result)                          # it has 2 fields data and error
    return jsonify(result.data)

@app.route("/todo/<id>", methods=["GET"])
def get_detail(id):
    todo = Todo.query.get(id)
    print(todo)
    return todo_schema.jsonify(todo)   #

@app.route("/todo/<id>", methods=["PUT"])
def update_todo(id):
    todo = Todo.query.get(id)
    task = request.form['task']
    todo.task = task
    done = request.form['done']
    print(done)
    
    if(done=='true'):
        done=True
    if(done=='false'):
        done=False
    todo.done = done
    db.session.commit()
    return todo_schema.jsonify(todo)


@app.route("/todo/<id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return todo_schema.jsonify(todo)


if __name__ == '__main__':
    app.run(debug=True)