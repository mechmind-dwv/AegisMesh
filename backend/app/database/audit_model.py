from sqlalchemy import Column, Integer, String

from app.database.database import Base

class AuditRecord(Base):

    __tablename__ = "audits"

    id = Column(Integer, primary_key=True, index=True)

    risk_score = Column(Integer)

    tracked_services = Column(String)

    recommendations = Column(String)
