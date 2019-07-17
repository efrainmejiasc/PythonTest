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

















