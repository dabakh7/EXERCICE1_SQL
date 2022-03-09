import mysql.connector 
import random

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Dabakh7.",
  database = "Exercice_BDD"
)
mycursor = mydb.cursor()

sql2 = "INSERT INTO PIECES(categorie,date,id_ref) VALUES (%s,%s,%s)"
val_Pieces=[]
Val_id_p=[]
mycursor.execute("Select id_ref from REFERENCE")
for b in mycursor.fetchall():
  Val_id_p.append(b[0])
for p in range(10):
  val_cat = random.choice(['Moteur','Eclairage','Freinage','Direction','Carrosserie','Echappement'])
  v_date = random.choice(['2021-3-12','2000-4-23','2006-5-25','2009-5-20','2021-2-1','1998-4-7'])
  val_id = random.choice(Val_id_p)
  val_Pieces.append((val_cat,v_date,val_id))
mycursor.executemany(sql2,val_Pieces)
mydb.commit()