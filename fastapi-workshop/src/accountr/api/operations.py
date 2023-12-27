# api/operations.py
from typing import List
from fastapi import APIRouter, Depends, Response, status
from .. import models
from ..services.operations import OperationsService

router = APIRouter(prefix='/operations', tags=['operations'])

@router.get('/', response_model=List[models.Operation])
def get_operations(wallet_id: int, operations_service: OperationsService = Depends()):
    return operations_service.get_many(wallet_id)

@router.post('/', response_model=models.Operation, status_code=status.HTTP_201_CREATED)
def create_operation(wallet_id: int, operation_data: models.OperationCreate, operations_service: OperationsService = Depends()):
    return operations_service.create(wallet_id, operation_data)

@router.get('/{operation_id}', response_model=models.Operation)
def get_operation(wallet_id: int, operation_id: int, operations_service: OperationsService = Depends()):
    return operations_service.get(wallet_id, operation_id)

@router.put('/{operation_id}', response_model=models.Operation)
def update_operation(wallet_id: int, operation_id: int, operation_data: models.OperationUpdate,
                     operations_service: OperationsService = Depends()):
    return operations_service.update(wallet_id, operation_id, operation_data)

@router.delete('/{operation_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_operation(wallet_id: int, operation_id: int, operations_service: OperationsService = Depends()):
    operations_service.delete(wallet_id, operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

