from flask import Flask, render_template, url_for, request, redirect
#? Importing all needed libraries from flask
from flask_sqlalchemy import SQLAlchemy
#? Importing the database
from datetime import datetime
#? Importing the date 

app = Flask(__name__) # ? This sets up the application
# Configure the database  (\\\ -> relative path, \\\\ -> absolute path)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#* --------------
# Calling the database and assigining it to a variable db.
db = SQLAlchemy(app)

""" To start the database 
Terminal 
    - Make sure to activate the environment // source env/bin/activate
    - write python3 on terminal and press enter
    - from app import db  
        - it is going to import the db variable that was create on line 13 | db = SQLAlchemy(app)
    - db.create_all()
        - creates the database
        - check in the workplace for the .db file
    - exit()
        - to exit the database
"""

class Todo(db.Model): # This is a model for the post (OOP)
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """This returns the tasks added"""
        return '<Task %r>' % self.id

#* Routes 
@app.route('/', methods=['POST', 'GET'])
def index():
    """ First route for the index page """
    if request.method == 'POST':
        # * "request" needs to be imported
        # If the request sent is a post, do something
        task_content = request.form['content'] # create a variable to get the value submitted in the form at "index.html"
        new_task = Todo(content=task_content) # create an object with the value fetched form "index.html"
        
        try:
            db.session.add(new_task) #try to add the values to the db.
            db.session.commit() #insert values to the db
            return redirect('/') #reload the page
            # * "redirect" -> needs to be imported 
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        # If the request is a GET then do this.
        # * all -> gets all of them / first -> most recent 
        return render_template('index.html', tasks=tasks) #Rendering the template, the path is templates/[file]
                                             #? task=task sends task to the update.html to be able to be accessed
@app.route('/delete/<int:id>')
        # ? delete the file and give the id 
        # ? (variable assigned in the line 29 inside the Todo class)
def delete(id):
    task_to_delete = Todo.query.get_or_404(id) # * Attempt to delete the item, if it doesnt find then it will give a 404 error
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Couldn't delete it."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
        # ? update the file and give the id 
        # ? (variable id was assigned in the line 29 inside the Todo class)
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error'
    else:
        return render_template('update.html', task=task) #? task=task sends task to the update.html to be able to be accessed

if __name__ == '__main__':
    app.run(debug=True) # debut=True shows the errors in the browser

