from sqlalchemy import BigInteger, Text, Float, JSON, Integer, Numeric, ARRAY;
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column;
from .base import AbsModel
class Sku(AbsModel):
    __tablename__ = 'sku';
    __table_arg__ = {'schema':'public'};

    product_id:Mapped[BigInteger] = mapped_column(BigInteger, default=0);
    title:Mapped[Text] = mapped_column(Text, default='-');
    description:Mapped[Text] = mapped_column(Text,default='-');
    brand:Mapped[Text] = mapped_column(Text,default='-');
    seller_id:Mapped[Integer] = mapped_column(Integer, default=0);
    seller_name:Mapped[Text] = mapped_column(Text, default='-');
    first_image_url:Mapped[Text] = mapped_column(Text, default='-');
    category_id:Mapped[Integer] = mapped_column(Integer, default='-');
    category_lvl_1:Mapped[Text] = mapped_column(Text, default = '-');
    category_lvl_2:Mapped[Text] = mapped_column(Text, default = '-');
    category_lvl_3:Mapped[Text] = mapped_column(Text, default = '-');
    category_remaining:Mapped[Text] = mapped_column(Text, default = '-');
    features:Mapped[JSON] = mapped_column(JSON, nullable=True);
    rating_count:Mapped[Integer] = mapped_column(Integer, default = 0);
    rating_value:Mapped[Numeric] = mapped_column(Numeric(precision=15, scale= 2), default = 0.0);
    price_before_discounts:Mapped[Float] = mapped_column(Float, default = 0.0);
    discount:Mapped[Numeric] = mapped_column(Numeric(precision=15, scale=2), default=0.0);
    price_after_discounts:Mapped[Float] = mapped_column(Float, nullable=True);
    bonuses:Mapped[Integer] = mapped_column(Integer, nullable=True);
    sales:Mapped[Integer] = mapped_column(Integer, default=0);
    currency:Mapped[Text] = mapped_column(Text, nullable = True);
    barcode:Mapped[Numeric] = mapped_column(Numeric(precision=25, scale=0), nullable = True);
    similar_sku:Mapped[ARRAY] = mapped_column(ARRAY(UUID),nullable = True);

__all__ = ('Sku')