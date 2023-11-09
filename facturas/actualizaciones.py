from modelos import Cliente, engine
from sqlalchemy.orm import sessionmaker

def registro(fila):
    print (fila.id, "Nombre: ", fila.nombre, "email:", fila.email, "¿esvip?", "si" if fila.vip else "No")
    
engine.echo = False
Session = sessionmaker (bind = engine)
sesion = Session()

print("\nMostramos el primer cliente no vip...")
novip = sesion.query(Cliente).filter(Cliente.vip==False).first()
registro(novip)

novip.vip = True
respuesta = input("Desea que sea vip? s/n")
if respuesta =="n":
    sesion.rollback()
else:
    sesion.commit()
print("Su estado ha quedado del siguiente modo:")
registro(novip)

print("\nVamos a cambiar todos los vip:")
vip = sesion.query(Cliente).filter(Cliente.vip==False).update({Cliente.vip:True})
sesion.commit()
for fila in sesion.query(Cliente).all():
    registro(fila)
print("\nDejaran de ser vip los clientes menores a 3")
novip2 = sesion.query(Cliente).filter(Cliente.id<3).update({Cliente.vip:False})
sesion.commit()
for fila in sesion.query(Cliente).all():
    registro(fila)