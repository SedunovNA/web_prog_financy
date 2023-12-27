from database import Base, engine

# Импортируйте все классы таблиц из tables.py
from tables import User, Operation, Wallet

# Создайте таблицы
Base.metadata.create_all(bind=engine)