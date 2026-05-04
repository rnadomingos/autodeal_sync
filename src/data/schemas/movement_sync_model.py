from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from data.infra.database import Base

class MovementSyncModel(Base):
  __tablename__ = 'movement_syncs'

  id = Column(Integer, primary_key=True, autoincrement=True)
  company_id = Column(Integer, nullable=False)
  status = Column(String, nullable=False)
  created_at = Column(DateTime(timezone=True), default=func.now())
  updated_at = Column(DateTime(timezone=True), default=func.now())