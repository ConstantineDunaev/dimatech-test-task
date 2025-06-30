from fastapi import APIRouter
from .user import user_router
from .account import account_router
from .transaction import transaction_router


router = APIRouter()

router.include_router(user_router)
router.include_router(account_router)
router.include_router(transaction_router)
