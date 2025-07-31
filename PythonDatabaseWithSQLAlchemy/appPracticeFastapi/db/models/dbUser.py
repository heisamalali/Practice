from sqlalchemy import Column, Integer, String

from PythonDatabaseWithSQLAlchemy.appPracticeFastapi.db.database import Base


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(500), nullable=False)