from flask import Flask
print(__name__)
#app here is an instance of the Class Flask.
app = Flask(__name__)

#"from app import routes" references the app directory as in Projects/microblog/app, so routes is a .py file that will be created in here!
from app import routes