from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.config import Base


class Account(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True, index=True)
    name = Column("nome_responsavel", String(50))
    transfer = relationship('Transfer')


class Transfer(Base):
    __tablename__ = 'transferencia'

    id = Column(Integer, primary_key=True, index=True)
    transfer_date = Column("data_transferencia", DateTime)
    value = Column(Float)
    type = Column(String(50))
    operator_name = Column(String(50))
    account_id = Column(Integer, ForeignKey('conta.id'))
    account = relationship('conta')
