from fastapi import FastAPI

from app.products.routers import router as product_router


app = FastAPI()

app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "Привет, мир"}
