from fastapi import FastAPI,HTTPException
from .db import Product,Order,SessionLocal,engine,Base
from contextlib import asynccontextmanager
from sqlalchemy import select
from typing import AsyncGenerator
from .model import ProductModel

# from sqlalchemy import 


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    # Connect to the database
    async with engine.begin() as conn:
        # Create all tables
        # print("session started")
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Close the database connection
    await engine.dispose()

app=FastAPI(lifespan=lifespan)



@app.post("/product")
async def post_product(product_model:ProductModel):
    product=Product(name=product_model.name,brand=product_model.brand,price=product_model.price,qty=product_model.qty,category=product_model.category)
    async with SessionLocal() as session:
            async with session.begin():
                session.add(product)
                p_id = await session.commit()
                return product.id

    


@app.get("/products")
async def get_products(category: str | None = None):
    if category:
         async with SessionLocal() as session:
            async with session.begin():
                stmt = stmt = select(*Product.__table__.columns).where(Product.category == category)
                result = await session.execute(stmt)
                record = result.all()
                x=[dict(row._mapping) for row in record]
                return x
    
    async with SessionLocal() as session:
        async with session.begin():
            stmt = select(*Product.__table__.columns)
            print(stmt)
            result = await session.execute(stmt)

            record = result.all()
            x=[dict(row._mapping) for row in record]
            return x
              

@app.post("/order")
async def order_product(product_id: int, qty: int):
    async with SessionLocal() as session:
        async with session.begin():

            product = await session.get(Product, product_id)
            if not product:
                return HTTPException(status_code=404,detail="Product not found")
            if product.qty < qty:
                return HTTPException(status_code=400,detail=f"Insufficient quantity. Maximum available: {product.qty}")
            
            order = Order(qty=qty, product_id=product_id)
            session.add(order)
            
            product.qty -= qty
            
            await session.commit()
            return {"order_id": order.id}



@app.get("/order/{order_id}")
async def get_order_id(order_id:int):
    if order_id:
        async with SessionLocal() as session:
            async with session.begin():
                stmt = stmt = select(*Order.__table__.columns,Product.name,Product.brand,Product.category).join(Product,Order.product_id==Product.id).where(Order.id == order_id)
                result = await session.execute(stmt)
                record = result.all()
                if not record:
                    return HTTPException(status_code=404,detail="Order not found")
                order_details=dict(record[0]._mapping)
                return order_details
    
