from flaskr.infrastructure.database import database


class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
