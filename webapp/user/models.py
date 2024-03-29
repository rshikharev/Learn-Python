from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(128), index=True)


    def __repr__(self) -> str:
        return '<User {}>'.format(self.username)
    

    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    
    @property
    def is_admin(self):
        return self.role == 'admin'