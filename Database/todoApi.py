from flask import Flask
from flask import g
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
import json
from json import JSONDecoder

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoDatabase.db'
db = SQLAlchemy(app)

class Encoder(JSONDecoder):
    def default(self, o):
        return o.__dict__

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(120), index = True)
    completed = db.Column(db.Integer)
    hasDue = db.Column(db.Integer)
    dueDate = db.Column(db.String(64))

    def toJson(self):
        return dict(id=self.id, title=self.title, description=self.description, hasDue=self.hasDue, dueDate=self.dueDate, completed=self.completed)

    def __repr__(self):
        return '<Title {}>'.format(self.title)

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

@app.route("/todos", methods=['GET', 'POST'])
def index():
    if(request.method == 'GET'):
        r = []
        for t in Todo.query.all():
            r.append(t.toJson())
        return(jsonify(r))
    elif(request.method == 'POST'):
        post = request.json
        newTodo = Todo(title=post.get("title"), description=post.get("description"), hasDue=post.get("hasDue"), dueDate=post.get("dueDate"), completed=post.get("completed"))
        db.session.add(newTodo)
        db.session.commit()
        response = app.response_class(response=newTodo.toJson(),
                                  status=200,
                                  mimetype='application/json')
        r = []
        for t in Todo.query.all():
            r.append(t.toJson())
        return(jsonify(newTodo.toJson()))        
    return ""

@app.route("/todos/<theid>", methods=['GET', 'DELETE'])
def id(theid):  
    if request.method == 'GET':     
        for t in Todo.query.all():
            if t.id == id:
                return t.toJson()
        return ""   
    elif request.method == 'DELETE':
        todo = Todo.query.filter(Todo.id==theid).delete()
        db.session.commit()
    return ""    

    
if __name__ == '__main__':
    app.run()