from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time, Date, SmallInteger, Text, VARCHAR
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = "users"

    id = Column(String, autoincrement=True, primary_key=True, index=True)
    role = Column(VARCHAR(3), nullable=False)
    name = Column(String, index=False, nullable=False)
    phone = Column(String, index=False, nullable=False)
    password = Column(String,index=False, nullable=False)


class Oferta(Base):
    __tablename__ = "oferta"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, index=False, nullable=False)
    charatistic = Column(String, index=False, nullable=False) #ТУТ ДОХУЯ СТОЛБИКОВ С ХАРАКТЕРИСТИКАМИ
    id_hozyain = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False, index=False)
class Zayavka(Base):
    __tablename__ = "zayavka"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    text=Column()
    id_raba=Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False, index=False)
    project_id=Column(Integer, ForeignKey(Oferta.id, ondelete="CASCADE"), nullable=False, index=False)
