from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .routers import router
from .schemas.error import Error
from .exceptions.user import AuthenticationError, PermissionDenied

app = FastAPI()

app.include_router(router)


@app.exception_handler(AuthenticationError)
async def exception_handler(_: Request, exc: AuthenticationError):
    return JSONResponse(status_code=401,
                        content=Error(error=str(exc)).dict())


@app.exception_handler(PermissionDenied)
async def exception_handler(_: Request, exc: PermissionDenied):
    return JSONResponse(status_code=403,
                        content=Error(error=str(exc)).dict())

