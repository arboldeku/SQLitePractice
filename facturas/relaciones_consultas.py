from modelos import Cliente, Factura, engine

from sqlalchemy.orm import  sessionmaker
Session = sessionmaker(bind = engine)
sesion = Session()

print("\nClientes con facturas")
for c, f in sesion.query(Cliente, Factura).filter(
    Cliente.id == Factura.id_cliente).all():
    print("ID: {} Nombre: {} Nº Factura: {} Total: {}".format(c.id, c.nombre, f.id, f.total))

confacturas = sesion.query(Cliente).join(Factura).filter(Factura.total>200)
print("\nClientes con facturas (join):")
for reg in confacturas:
    for fac in reg.misfacturas:
        print("xID: {} Nombre: {} nº Factura {} Total: {}".format(reg.id, reg.nombre, fac.id, fac.total))
        
engine.echo = False
todos = sesion.query(Cliente).outerjoin(Factura)
print("\nTodos los clientes y sus facturas")
for reg in todos:
    print("xID: {} Nombre: {}".format(reg.id, reg.nombre))
    for fac in reg.misfacturas:
        print("---Nº Factura: {} Total: {}".format(fac.id, fac.total))