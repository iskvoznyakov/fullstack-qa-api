class ApiException(Exception):
    """Базовое исключение для ошибок при работе с API"""
    pass


class UnauthorizedException(ApiException):
    """Ошибка 401 — нет авторизации"""
    pass


class NotFoundException(ApiException):
    """Ошибка 404 — ресурс не найден"""
    pass


class ServerErrorException(ApiException):
    """Ошибка 5xx — ошибка сервера"""
    pass
