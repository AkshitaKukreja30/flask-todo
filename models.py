from app import *

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
    def __init__(self):
    	pass
        

# todo_schema = TodoSchema()
# todos_schema = TodoSchema(many=True)

