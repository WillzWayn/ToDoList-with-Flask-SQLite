from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


migrate = Migrate(app,
                  db)  # quero instanciar o migrate e ele vai cuidar das minha migrações, ela precisa receber a aplcação e o bd

manager = Manager(app)  # Cuida dos comandos
manager.add_command('db', MigrateCommand)


from app.models import tables
from app.controllers import routes
