from app import *

@app.route("/todo", methods=["POST"])
def add_todo():
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