from fastapi import APIRouter
from .me import me_router
from .user import user_router
from .account import account_router
from .transaction import transaction_router
from .webhook import webhook_router


router = APIRouter()

router.include_router(me_router)
router.include_router(user_router)
router.include_router(account_router)
router.include_router(transaction_router)
router.include_router(webhook_router)

