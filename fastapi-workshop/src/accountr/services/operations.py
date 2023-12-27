# services/operations.py
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, tables
from ..database import get_session

class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self, wallet_id: int) -> List[tables.Operation]:
        operations = (
            self.session
            .query(tables.Operation)
            .filter(tables.Operation.wallet_id == wallet_id)
            .order_by(
                tables.Operation.date.desc(),
                tables.Operation.id.desc(),
            )
            .all()
        )
        return operations

    def get(self, wallet_id: int, operation_id: int) -> Optional[tables.Operation]:
        operation = (
            self.session
            .query(tables.Operation)
            .filter(
                tables.Operation.wallet_id == wallet_id,
                tables.Operation.id == operation_id,
            )
            .first()
        )
        if not operation:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Operation not found')
        return operation

    def create(self, wallet_id: int, operation_data: models.OperationCreate) -> tables.Operation:
        operation = tables.Operation(
            **operation_data.dict(),
            wallet_id=wallet_id,
        )
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, wallet_id: int, operation_id: int, operation_data: models.OperationUpdate) -> tables.Operation:
        operation = self.get(wallet_id, operation_id)
        if operation:
            for field, value in operation_data:
                setattr(operation, field, value)
            self.session.commit()
        return operation

    def delete(self, wallet_id: int, operation_id: int):
        operation = self.get(wallet_id, operation_id)
        if operation:
            self.session.delete(operation)
            self.session.commit()
