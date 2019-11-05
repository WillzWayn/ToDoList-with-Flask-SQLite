from app import db


class Tasks(db.Model):
    __tablename__= 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean)

    def __init__(self, content, done=False):
        self.content = content
        self.done = done