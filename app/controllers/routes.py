from flask import render_template, request, redirect, url_for
from app.models.tables import Tasks
from app import app,db


@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template('index.html', task_list = tasks)


@app.route('/new_task', methods=['POST'])
def create_task():
    task=Tasks(content=request.form['tarefatodo'])
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    (Tasks.query.filter_by(id=int(id)).delete())
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/mark/<id>')
def changeDone(id):
    task = (Tasks.query.filter_by(id=int(id)).first())
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('index'))
