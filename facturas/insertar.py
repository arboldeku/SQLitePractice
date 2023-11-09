from modelos import Cliente, engine

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
sesion = Session()

#cliente1 = Cliente(nombre = "Isabel Costa", email = "isac@correo.es", vip = False)

#sesion.add(cliente1)
sesion.add_all([
    Cliente(nombre = "Pedro Figueroa", email = "pfige@correo.es", vip = False),
    Cliente(nombre = "Nuria Cervera", email = "ncervera@correo.es", vip = True),
    Cliente(nombre = "Dana Asensio", email = "danaaese@correo.es", vip = False)
    ])
sesion.commit()