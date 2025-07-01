from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.routers import router
from app.schemas.error import Error
from app.exceptions import (AuthenticationError, PermissionDeniedError, EmailAlreadyExistsError, UserNotFoundError,
                            UserHasAccountsError, InvalidSingnatureError, AccountNotFoundError,
                            TransactionIDAlreadyExistsError)

app = FastAPI(docs_url=None,
              title="Тестовое задание Dimatech",
              description="Реализация REST API для тестового задания.",
              version="1.0.0")

app.include_router(router)


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=Error(error="Ошибка валидации",
                      details=str(exc)).dict(exclude_none=True)
    )


@app.exception_handler(AuthenticationError)
async def authentication_handler(_: Request, exc: Exception):
    return JSONResponse(status_code=401,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(InvalidSingnatureError)
async def invalid_signature_handler(_: Request, exc: Exception):
    return JSONResponse(status_code=401,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(PermissionDeniedError)
async def permission_denied_handler(_: Request, exc: PermissionDeniedError):
    return JSONResponse(status_code=403,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(UserNotFoundError)
async def user_not_found_handler(_: Request, exc: UserNotFoundError):
    return JSONResponse(status_code=404,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(AccountNotFoundError)
async def account_not_found_handler(_: Request, exc: AccountNotFoundError):
    return JSONResponse(status_code=404,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(EmailAlreadyExistsError)
async def email_already_exists_handler(_: Request, exc: EmailAlreadyExistsError):
    return JSONResponse(status_code=409,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(UserHasAccountsError)
async def user_has_accounts_handler(_: Request, exc: UserHasAccountsError):
    return JSONResponse(status_code=409,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(TransactionIDAlreadyExistsError)
async def transaction_id_already_exists_handler(_: Request, exc: TransactionIDAlreadyExistsError):
    return JSONResponse(status_code=409,
                        content=Error(error=str(exc)).dict(exclude_none=True))
