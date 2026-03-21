"""Исключения приложения + Litestar exception handlers."""
from litestar import Request, Response
from litestar.status_codes import (
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
    HTTP_429_TOO_MANY_REQUESTS,
    HTTP_502_BAD_GATEWAY,
)


# ---------------------------------------------------------------------------
# Доменные исключения
# ---------------------------------------------------------------------------

class OzonCollectorException(Exception):
    pass


class ObjectNotFoundException(OzonCollectorException):
    pass


class ObjectAlreadyExistsException(OzonCollectorException):
    pass


class OzonApiException(OzonCollectorException):
    def __init__(self, status_code: int, message: str = ""):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Ozon API error {status_code}: {message}")


class OzonApiRateLimitException(OzonApiException):
    pass


class OzonApiUnauthorizedException(OzonApiException):
    pass


# ---------------------------------------------------------------------------
# Litestar exception handlers
# ---------------------------------------------------------------------------

def not_found_handler(_: Request, exc: ObjectNotFoundException) -> Response:
    return Response(
        content={"error": "not_found", "detail": str(exc) or "Object not found"},
        status_code=HTTP_404_NOT_FOUND,
    )


def already_exists_handler(_: Request, exc: ObjectAlreadyExistsException) -> Response:
    return Response(
        content={"error": "already_exists", "detail": str(exc)},
        status_code=HTTP_409_CONFLICT,
    )


def ozon_api_handler(_: Request, exc: OzonApiException) -> Response:
    if isinstance(exc, OzonApiRateLimitException):
        status = HTTP_429_TOO_MANY_REQUESTS
    elif isinstance(exc, OzonApiUnauthorizedException):
        status = HTTP_401_UNAUTHORIZED
    else:
        status = HTTP_502_BAD_GATEWAY
    return Response(
        content={"error": "ozon_api_error", "status_code": exc.status_code, "detail": exc.message},
        status_code=status,
    )


EXCEPTION_HANDLERS = {
    ObjectNotFoundException: not_found_handler,
    ObjectAlreadyExistsException: already_exists_handler,
    OzonApiException: ozon_api_handler,
}
