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



DB_NAME = 'test'
TABLES={}
TABLES['testpython']=(
  "CREATE TABLE 'testpython' ("
  " 'idTestPython' INT NOT NULL AUTO_INCREMENT,"
  " 'nombre' VARCHAR(45) NULL,"
  " 'edad' INT NULL,"
  " 'departamento' VARCHAR(45) NULL,"
  " 'salario' DOUBLE NULL,"
  " 'fecha' DATE NULL,"
  "PRIMARY KEY ('idTestPython')ENGINE=InnoDB")


print(TABLES)














