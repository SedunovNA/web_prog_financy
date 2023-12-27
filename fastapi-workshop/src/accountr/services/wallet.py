# services/wallet.py
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, tables
from ..database import get_session

class WalletService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self) -> List[tables.Wallet]:
        return self.session.query(tables.Wallet).all()

    def get(self, wallet_id: int) -> Optional[tables.Wallet]:
        return self.session.query(tables.Wallet).filter(tables.Wallet.id == wallet_id).first()

    def create(self, wallet_data: models.WalletCreate) -> tables.Wallet:
        wallet = tables.Wallet(**wallet_data.dict())
        self.session.add(wallet)
        self.session.commit()
        return wallet

    def update(self, wallet_id: int, wallet_data: models.WalletUpdate) -> Optional[tables.Wallet]:
        wallet = self.get(wallet_id)
        if wallet:
            for field, value in wallet_data:
                setattr(wallet, field, value)
            self.session.commit()
        return wallet

    def delete(self, wallet_id: int):
        wallet = self.get(wallet_id)
        if wallet:
            self.session.delete(wallet)
            self.session.commit()
