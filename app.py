from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
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

from routes import *



if __name__ == '__main__':
    app.run(debug=True)