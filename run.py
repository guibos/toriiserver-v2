from flaskr.infrastructure.database.db import init_db
from flaskr.main import app
if __name__ == "__main__":
    init_db()
    app.run()
