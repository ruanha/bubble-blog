from flask import Flask
from config import Config

#app here is an instance of the Class Flask.
app = Flask(__name__)
app.config.from_object(Config)

#"from app import routes" references the app directory as in Projects/microblog/app, so routes is a .py file that will be created in here!
from app import routes