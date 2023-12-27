# models/wallet.py
from typing import List
from decimal import Decimal
from pydantic import BaseModel, PositiveInt
from .operations import Operation

class WalletCreate(BaseModel):
    name: str
    currency: str

class Wallet(BaseModel):
    id: PositiveInt
    name: str
    currency: str
    operations: List[Operation] = []  # Assuming you have an Operation model

class WalletUpdate(BaseModel):
    name: str
    currency: str
