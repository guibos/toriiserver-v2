from flask_sqlalchemy import SQLAlchemy

from flaskr.main import app


database = SQLAlchemy(app)
