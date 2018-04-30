from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#app here is an instance of the Class Flask.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#"from app import routes" references the app directory as in Projects/microblog/app, so routes is a .py file that will be created in here!
from app import routes, models