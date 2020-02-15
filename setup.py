import logging

from src.infrastructure.database import base
from src.infrastructure.database.models.title_model import TitleModel
from src.infrastructure.database.models import UserModel

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    log.info("Database")
    base.Base.metadata.create_all(base.engine)
    users = [
        {'username': 'admin', 'id': 1},
        {'username': 'guibos', 'id': 2},
    ]
    titles = [
        {'name': 'Top Gun', 'user_id': 2},
        {'name': 'Fate', 'user_id': 2},
    ]
    for user_dict in users:
        user = UserModel(**user_dict)
        base.db_session.add(user)

    base.db_session.commit()

    for title_dict in titles:
        title = TitleModel(**title_dict)
        base.db_session.add(title)

    base.db_session.commit()