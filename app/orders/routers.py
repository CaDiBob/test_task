from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.exceptions import (
    ProductInsufficientQuantityException,
    OrderNotFoundException,
)
from app.orders.dao import OrderDAO
from app.orders.schemas import OrderItemShema, OrderOutSchema, OrderSchema
from app.orders.services import OrderAddService, OrderGetService
from app.orders.dependencies import get_current_status
from app.products.schemas import ErrorMessageSchema


router = APIRouter(
    prefix='/orders',
    tags=['Oprders'],
)


@router.post(
    '',
    responses={
        status.HTTP_409_CONFLICT: {'model': ErrorMessageSchema},
    },
)
async def add_order(order_items: list[OrderItemShema]) -> OrderSchema:
    try:
        service = OrderAddService(order_items)
        order_id = await service.add_order()
    except ProductInsufficientQuantityException as e:
        return JSONResponse(
            {'message': str(e)},
            status_code=status.HTTP_409_CONFLICT,
        )
    return {'order_id': order_id}


@router.get('')
async def get_orders() -> list[OrderOutSchema]:
    service = OrderGetService()
    return await service.get_orders()


@router.get(
    '/{order_id}',
    responses={
        status.HTTP_404_NOT_FOUND: {'model': ErrorMessageSchema},
    },
)
async def get_order(order_id: int) -> OrderOutSchema:
    try:
        service = OrderGetService()
        return await service.get_order(order_id=order_id)
    except OrderNotFoundException as e:
        return JSONResponse(
            content={'message': str(e)},
            status_code=status.HTTP_404_NOT_FOUND,
        )


@router.patch(
    '/{order_id}/{status}'
)
async def update_order_status(
    order_id: int,
    status: str = Depends(get_current_status),
) -> dict:
    await OrderDAO.update(order_id, status=status)
    return {'message': f'у заказа id {order_id} новый статус {status}'}
