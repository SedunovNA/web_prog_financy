# api/wallet.py
from fastapi import APIRouter, Depends, HTTPException, status
from .. import models
from ..services.wallet import WalletService
from typing import List

router = APIRouter(prefix='/wallet', tags=['wallet'])

@router.get('/', response_model=List[models.Wallet])
def get_wallets(wallet_service: WalletService = Depends()):
    return wallet_service.get_all()

@router.get('/{wallet_id}', response_model=models.Wallet)
def get_wallet(wallet_id: int, wallet_service: WalletService = Depends()):
    wallet = wallet_service.get(wallet_id)
    if wallet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Wallet not found')
    return wallet

@router.post('/', response_model=models.Wallet, status_code=status.HTTP_201_CREATED)
def create_wallet(wallet_data: models.WalletCreate, wallet_service: WalletService = Depends()):
    return wallet_service.create(wallet_data)

@router.put('/{wallet_id}', response_model=models.Wallet)
def update_wallet(wallet_id: int, wallet_data: models.WalletUpdate, wallet_service: WalletService = Depends()):
    wallet = wallet_service.update(wallet_id, wallet_data)
    if wallet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Wallet not found')
    return wallet

@router.delete('/{wallet_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_wallet(wallet_id: int, wallet_service: WalletService = Depends()):
    wallet_service.delete(wallet_id)
