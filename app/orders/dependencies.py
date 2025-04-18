from app.exceptions import StatusInvalidException
from app.orders.models import Status


def get_current_status(status: str):
    if status not in Status.__args__:
        raise StatusInvalidException
    return status
