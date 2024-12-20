from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

class ProductEnum(str, Enum):
        ZAPFLOW_GEMINI = "Zapflow with Gemini"
        ZAPFLOW_CHATGPT = "Zapflow with chatGPT"
        ZAPFLOW_LLAMA = "Zapflow with Lhama 3.0"

class Sales(BaseModel):
    """
    Data model for sales.

    Args:
        email (EmailStr): Client's email address
        date (datetime): Sale date
        product (ProductEnum): Product category
        price (PositiveFloat): Product price
        quantity (PositiveInt): Product quantity
    """
    email: EmailStr
    date: datetime
    product: ProductEnum
    price: PositiveFloat
    quantity: PositiveInt

