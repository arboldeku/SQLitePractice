from modelos import Cliente, Factura, engine

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
sesion = Session()

def listado (consulta):
    for reg in consulta:
        print ("ID: {} Nombre {}".format(reg.id, reg.nombre))
        for fac in reg.misfacturas:
            print("---Nº factura: {} Total: {}".format(fac.id, fac.total))

engine.echo = False
print("\nListado de clientes y facturas:")
todos = sesion.query(Cliente).outerjoin(Factura).order_by(Cliente.id)
listado(todos)

num = input("Indique numero de cliente a borrar: ")
sesion.delete(sesion.query(Cliente).get(num))
print("\nListado resultante:")
listado(todos)
confir = input("¿Efectuar eliminacion? (s/n)")
if confir =="s":
    sesion.commit()
else:
    sesion.rollback()