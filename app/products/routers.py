from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.products.dao import ProductDAO
from app.products.schemas import ProductSchema, ErrorMessageSchema


router = APIRouter(
    prefix='/products',
    tags=['Products'],
)


@router.post('', status_code=status.HTTP_201_CREATED)
async def add_product(new_product: ProductSchema) -> ProductSchema:
    await ProductDAO.add(**new_product.model_dump())
    return new_product


@router.get('')
async def get_products() -> list[ProductSchema]:
    return await ProductDAO.find_all()


@router.get(
    '/{product_id}',
    responses={
        status.HTTP_404_NOT_FOUND: {'model': ErrorMessageSchema},
    }
)
async def get_product(product_id: int) -> dict:
    product = await ProductDAO.find_one_or_none(id=product_id)
    if not product:
        return JSONResponse(
            content={'message': 'not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return product


@router.put(
    '/{product_id}',
    responses={
        status.HTTP_404_NOT_FOUND: {'model': ErrorMessageSchema},
    }
)
async def update_product(
    product_id: int,
    updated_product: ProductSchema,
) -> dict:
    product = await ProductDAO.update(
        product_id,
        **updated_product.model_dump(),
    )
    product = await ProductDAO.find_one_or_none(id=product_id)
    if not product:
        return JSONResponse(
            content={'message': 'not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return product


@router.delete(
    '/{product_id}',
    responses={
        status.HTTP_404_NOT_FOUND: {'model': ErrorMessageSchema},
    }
)
async def delete_product(product_id: int) -> dict:
    product = await ProductDAO.find_one_or_none(id=product_id)
    if not product:
        return JSONResponse(
            content={'message': 'not found'},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    product = await ProductDAO.delete(product_id)
    return {'message': 'deleted'}
