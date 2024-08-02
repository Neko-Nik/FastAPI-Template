"""
Database models for the email logs and relational email logs.
"""

from src.utils.base.libraries import declarative_base, Column, String, Integer, ForeignKey, DateTime, JSON, relationship, datetime


Base = declarative_base()


class NekoData(Base):
    __tablename__ = 'neko_nik_data'

    uid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, index=True, default=datetime.now)
    meta_data = Column(JSON, nullable=False, default={})
