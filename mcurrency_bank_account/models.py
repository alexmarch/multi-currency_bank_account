from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, DECIMAL
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.orm import relationship, validates
from app import db, login_manager, bcrypt
from datetime import datetime

currency = {
    'USD': 'USD',
    'GBP': 'GBP',
    'EUR': 'EUR',
    'JPY': 'JPY',
    'RUB': 'RUB'
}
# User model

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, index=True, nullable=False)
    _password = Column(String(100))
    banks = relationship('Bank', lazy='joined')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
       self._password = bcrypt.generate_password_hash(password, 10)

    @hybrid_method
    def is_correct_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id).encode('utf-8')

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))

# Bank model
class Bank(db.Model):
    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True)
    currency = Column(String(8), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, back_populates='banks')
    amount = Column(DECIMAL(13, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

    @validates('currency')
    def validate_currency(self, key, banks):
        assert banks in currency, 'Currency not valid.'
        return banks

    def __init__(self, currency, user_id, user, amount):
        self.currency = currency
        self.user_id = user_id
        self.user = user
        self.amount = amount

    def serializer(self):
        return { 'username': self.user.username, 'currency': self.currency, 'amount': float(self.amount) }

    def __repr__(self):
        return '<Bank %r, %r, %r>' % (self.user_id, self.currency, self.amount)
