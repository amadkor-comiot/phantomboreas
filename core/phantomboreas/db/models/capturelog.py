from sqlalchemy import Column, Integer, LargeBinary, String, Float, DateTime
from sqlalchemy.dialects.mysql import MEDIUMBLOB
from sqlalchemy.orm import relationship

from base import Base



class CaptureLog(Base):
    __tablename__ = 'capture_log'

    id = Column(Integer, primary_key=True)

    filepath        = Column(String)
    filename        = Column(String(256))
    latitude        = Column(Float)
    longitude       = Column(Float)
    timestamp       = Column(DateTime)

    plates = relationship("PlateLog", back_populates="capture")
