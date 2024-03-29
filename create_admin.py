from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db

app = create_app()

with app.app_context():
    username = input('Введите имя:')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже существует')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f'Создан пользлватель с id={new_user.id}')