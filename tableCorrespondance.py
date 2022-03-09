import mysql.connector 
import random

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Dabakh7.",
  database = "Exercice_BDD"
)
mycursor = mydb.cursor()

sql3 = "INSERT INTO CORRESPOND(id_piece,id_veh) VALUES (%s,%s)"
Valeur_idp =[]
Valeur_idv =[]
Val_final_cor =[]
mycursor.execute("Select id_piece from PIECES")
for  a in mycursor.fetchall():
  Valeur_idp.append(a[0])
mycursor.execute("Select id_veh from VEHICULES")
for b in mycursor.fetchall():
  Valeur_idv.append(b[0])
for s in range(10):
  V_p=random.choice(Valeur_idp)
  V_pi=random.choice(Valeur_idv)
  Val_final_cor.append((V_p,V_pi))
mycursor.executemany(sql3,Val_final_cor)
mydb.commit()
