from sqlalchemy.orm import mapped_column,Mapped, DeclarativeBase;
from sqlalchemy import func;
from pydantic.types import UUID4
from datetime import datetime;
from sqlalchemy.dialects.postgresql import UUID;
import uuid

class AbsModel(DeclarativeBase):

    uuid:Mapped[UUID4] = mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4, nullable = False);
    inserted_at:Mapped[datetime] = mapped_column(default = datetime.utcnow())
    updated_at:Mapped[datetime] = mapped_column(default = datetime.utcnow(), onupdate=func.now());


