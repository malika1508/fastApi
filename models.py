from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from sqlalchemy.sql.functions import user

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable= False)
    content = Column(String, nullable= False)
    published = Column(Boolean, server_default = 'TRUE')
    ownerId = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable= False)

    # items = relationship("Item", back_populates="owner")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True)
    email = Column(String, nullable = False, unique= True)
    password = Column(String, nullable = False)
