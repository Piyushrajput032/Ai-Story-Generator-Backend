from sqlalchemy import Column,Integer,String,DateTime,Boolean,ForeignKey,JSON

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base


class Story(Base):
    __tablename__="stories"

    id=Column(Integer,primary_key=True,index=True)
    