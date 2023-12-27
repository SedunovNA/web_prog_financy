from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    wallet = relationship('Wallet', back_populates='owner')


class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'), index=True)  # Добавлено отношение к кошельку
    date = Column(Date)
    kind = Column(String)
    amount = Column(Numeric(10, 2))
    description = Column(String, nullable=True)

    user = relationship('User', backref='operations')
    wallet = relationship('Wallet', back_populates='operations')  # Добавлено отношение к кошельку


class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Добавлено поле name
    currency = Column(String)  # Добавлено поле currency
    owner_id = Column(Integer, ForeignKey('users.id'))
    balance = Column(Numeric(10, 2), default=0)

    owner = relationship('User', back_populates='wallet')
    operations = relationship('Operation', back_populates='wallet') # Добавлено отношение к операциям

