from pydantic import BaseModel;
from typing import Optional
from pydantic.types import UUID, Any
class Sku(BaseModel):
    uuid: Optional[UUID];
    product_id:Optional[int];
    title:Optional[str];
    description:Optional[str];
    brand:Optional[str];
    seller_id:Optional[int];
    seller_name:Optional[str];
    first_image_url:Optional[str];
    category_id:Optional[int];
    category_lvl_1:Optional[str];
    category_lvl_2:Optional[str];
    category_lvl_3:Optional[str];
    category_remaining:Optional[str];
    features: Optional[dict];
    rating_count:Optional[int];
    rating_value:Optional[float];
    price_before_discounts:Optional[float] = None;
    discount:Optional[float];
    price_after_discounts:Optional[float] = None;
    bonuses:Optional[int]|None;
    sales:Optional[int];
    currency:Optional[str];
    barcode:Optional[float];
    similar_sku:Optional[list] | None
    class Config:
       from_attributes = True;
