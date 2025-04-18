from fastapi import HTTPException, status


class AppBaseException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'Внутренняя ошибка сервера'

    def __init__(self) -> None:
        super().__init__(
            status_code=self.status_code,
            detail=self.detail,
        )


class ProductInsufficientQuantityException(Exception):
    """Ошибка, если на складе не достаточно продукта"""


class ProductNotFoundException(Exception):
    """Ошибка, если продукт не найден"""


class OrderNotFoundException(Exception):
    """Ошибка, если заказ не найден"""


class StatusInvalidException(AppBaseException):
    """Ошибка, если статус невалидный"""
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Статус может быть processing, sending, delivered'
