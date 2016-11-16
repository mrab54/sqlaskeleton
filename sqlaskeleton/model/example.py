import datetime
from sqlalchemy import Integer, DateTime, Column, Boolean

from sqlaskeleton.model import Base


class Example(Base):
    __tablename__ = 'example'
    __table_args__ = {'schema': 'sqlaskeleton'}

    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean, default=False, nullable=False)
    date_added = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.now)
