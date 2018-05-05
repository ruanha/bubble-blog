import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

#to actually use these you need to export them to the environment.
#to test locally use the SMTP python debugging mail server
#(venv) rune@rune-desktop:~/Projects/microblog$ python -m smtpd -n -c DebuggingServer localhost:8025
	MAIL_SERVER = os.environ.get("MAIL_SERVER")
	MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
	MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	ADMINS = ["my-email@example.com"]
    