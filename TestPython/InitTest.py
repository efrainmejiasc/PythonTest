numero = 3 
final = 11
for x in range(numero,final):
    print("Posicion " + str(x - numero))
    print("Jugador" + str(x))

msg ="Efrain Mejias Castillo"
print (msg)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

print (mydb)

cnx = mysql.connector.connect(host='127.0.0.1',user='root',passwd='root', database='gig')
cnxCursor = cnx.cursor()
cnxCursor.execute("CREATE TABLE testpython (id INT NOT NULL AUTO_INCREMENT,name VARCHAR(255), apellido VARCHAR(255), edad INT , salario DOUBLE , fecha DATE,PRIMARY KEY (id))")


cnxCursor.execute("show databases")
for tabla in cnxCursor:
    print(tabla)



cnxCursor.close()













