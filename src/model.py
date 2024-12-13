from pydantic import BaseModel

class ProductModel(BaseModel):
    name : str
    brand : str
    price : float
    qty : int
    category : str