from db import db_session
from models import User

user = User(name='Oxana Tsikina', salary=200000, email='otsikina@example.ru')
db_session.add(user)
db_session.commit()