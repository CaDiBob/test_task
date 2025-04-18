from fastapi import FastAPI

from app.orders.routers import router as order_router
from app.products.routers import router as product_router


app = FastAPI()

app.include_router(product_router)
app.include_router(order_router)


@app.get("/")
async def root():
    return {"message": "Привет, мир"}
