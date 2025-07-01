from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.routers import router
from app.schemas.error import Error
from app.exceptions.user import AuthenticationError, PermissionDenied, EmailAlreadyExistsError, UserNotFoundError

app = FastAPI()

app.include_router(router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=Error(error="Ошибка валидации",
                      details=str(exc)).dict(exclude_none=True)
    )


@app.exception_handler(AuthenticationError)
async def exception_handler(_: Request, exc: AuthenticationError):
    return JSONResponse(status_code=401,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(PermissionDenied)
async def exception_handler(_: Request, exc: PermissionDenied):
    return JSONResponse(status_code=403,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(EmailAlreadyExistsError)
async def exception_handler(_: Request, exc: EmailAlreadyExistsError):
    return JSONResponse(status_code=409,
                        content=Error(error=str(exc)).dict(exclude_none=True))


@app.exception_handler(UserNotFoundError)
async def exception_handler(_: Request, exc: UserNotFoundError):
    return JSONResponse(status_code=404,
                        content=Error(error=str(exc)).dict(exclude_none=True))
