from app.dao.base import BaseDAO
from app.products.models import ProductModel


class ProductDAO(BaseDAO):
    model = ProductModel
