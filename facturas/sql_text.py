from modelos import Cliente, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

def listado(consulta):
    for fila in consulta:
        print(fila.id, "Nonbre:", fila.nombre, "email:", fila.email, "¿es vip?", "Si" if fila.vip else "NO")
    
engine.echo = False
Session = sessionmaker (bind = engine)
sesion = Session()


print("\nMostramos los clientes con id > 2:")
cli = sesion.query(Cliente).filter(text("id>2"))
listado(cli)

mi_id = input("¿Que id de cliente quieres consultar? ")
consulta = sesion.query(Cliente).filter(text ("id = :valor")).params(valor = mi_id).scalar()

if consulta:
    print("Su nombre es", consulta.nombre)
else:
    print("Ese cliente no se ha encontrado")

print("\nPodemos indicar instrucciones SQL directamente:")
todos = sesion.query(Cliente).from_statement(text("SELECT * FROM clientes"))
listado (todos)
print("\nPero cuando no son de seleccion, hemos de emplear execute", 
      "por ejemplo para cambiar a no VIP^al cliente cervera:")
sesion.execute("UPDATE clientes SET vip=False WHERE nombre LIKE '% Cervera'")
sesion.commit()
listado(todos)