from conexion import engine
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)
    vip = Column(Boolean)

class Factura(Base):
    __tablename__ = "facturas"
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id"))
    concepto = Column(String)
    total = Column(Float)

Cliente.misfacturas = relationship("Factura", order_by = Factura.id, backref="clientes",
                                   cascade="all, delete-orphan")
    
Base.metadata.create_all(engine)