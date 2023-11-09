from modelos import Cliente, engine
from sqlalchemy.orm import sessionmaker

def listado(consulta):
    for fila in consulta:
        print(fila.id, "Nombre: ", fila.nombre, "email:", fila.email, "¿es VIP?:", "Sí" if fila.vip else "NO")
        
Session = sessionmaker(bind = engine)
sesion = Session()
result = sesion.query(Cliente).all()
print("Listado completo de clientes:")
listado(result)

novip = sesion.query(Cliente).filter(Cliente.vip==False)
print("\nListado de clientes no vip:")
listado(novip)

from sqlalchemy import and_, or_
engine.echo=False
print("\nAplicacion de Like (nombres que terminen en Costa):")
costa = sesion.query(Cliente).filter(Cliente.id.in_((1,3)))

print("\nAplicacion de in(id en lista (1,3):")
unoytres = sesion.query(Cliente).filter(Cliente.id.in_((1,3)))
listado(unoytres)

print("\nAplicacion de and (vip==False y id>1):")
vipid = sesion.query(Cliente).filter(and_(Cliente.vip==False, Cliente.id>1))
listado(vipid)

print("\nAplicacion de and (Variante sin funcion):")
vipid2 = sesion.query(Cliente).filter(Cliente.vip==False, Cliente.id>1)
listado(vipid2)

print("\nAplicacion de or (vip==True o apellido comience por C):")
vipid3 = sesion.query(Cliente).filter(or_(Cliente.vip==True, Cliente.nombre.like("% C")))
listado(vipid3)

vips= sesion.query(Cliente).filter(Cliente.vip).first()
print("\nNombre del primer cliente vip:", vips.nombre)

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
resultado = sesion.query(Cliente).filter(Cliente.nombre.like("%Federico%"))
print("\nCantidad de clientes:", resultado.count())
try:
    if resultado.one():
        print("El nombre es:", resultado.nombre)
    else:
        print("Ningun resultado")
except NoResultFound:
    print("Ningun resultado.")
except MultipleResultsFound:
    print("Mas de un resultado encontrado.")
    
    
    
