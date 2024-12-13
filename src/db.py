from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import Optional,List
from sqlalchemy import DateTime,ForeignKey,String,Integer,Float,Boolean
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
import datetime
from dotenv import load_dotenv
import os

load_dotenv()



engine = create_async_engine(
    os.getenv("DATABASE_URL"), pool_size=20, max_overflow=0
)

SessionLocal = async_sessionmaker(
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product"
    id = mapped_column(Integer,primary_key=True,index=True)
    name = mapped_column(String(100))
    brand = mapped_column(String(50),index=True)
    price = mapped_column(Float)
    qty = mapped_column(Integer)
    category = mapped_column(String(50),index=True)

    order = relationship("Order", back_populates="product")

class Order(Base):
    __tablename__ = "order"
    id = mapped_column(Integer,primary_key=True)
    creation = mapped_column(DateTime,default=datetime.datetime.now)
    product_id = mapped_column(ForeignKey("product.id"))
    qty = mapped_column(Integer)
    product = relationship("Product", back_populates="order")




