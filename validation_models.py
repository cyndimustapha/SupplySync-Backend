from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductModel(BaseModel):
    name: str
    sku: str
    price: int
    stock: int

class TransactionModel(BaseModel):
    user_id: int
    product_id: int
    date: datetime
    quantity: int
    total_price: int
    type: str

class UserModel(BaseModel):
    email: str
    password: str
    companyName: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None

class LoginModel(BaseModel):
    email: str
    password: str