from modelos import Cliente, Factura, engine

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
sesion = Session()

nuevo = Cliente(nombre = "Esmeralda Borrallo", email = "esmb@correo.es", vip = False)

nuevo.misfacturas=[Factura(concepto="Alimentacion", total=245.45), Factura(concepto="Hogar", total=330.85)]

print("Creamos un nuevocliente y añadimos dos facturas")
sesion.add(nuevo)
sesion.commit()

fact = Factura(concepto="Juguetes", total=120.55)
costa = sesion.query(Cliente).filter(Cliente.nombre.like("%Costa")).scalar()
if costa:
    costa.misfacturas.append(fact)
    sesion.commit()
    print("Hemos añadido una factura a Costa")
else:
    print("Se ha buscado al cliente Costa pero no se ha encontrado")