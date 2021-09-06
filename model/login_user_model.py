from datetime import datetime
from sqlalchemy import Column, String, DateTime
from database.database import Base


class LoginUser(Base):
    __tablename__ = 'final_login_user'

    id = Column(String(50), primary_key=True)
    password = Column(String(500), nullable=False)
    type = Column(String(50), nullable=False, default='basic')
    description = Column(String(500), nullable=True)
    reg_dt = Column(DateTime(timezone=True), default=datetime.utcnow)
