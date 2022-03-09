import mysql.connector 
import random

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Dabakh7.",
  database = "Exercice_BDD"
)
mycursor = mydb.cursor()

sql1 = "INSERT INTO REFERENCE(prix) VALUE (%s)"
val_Ref=[]
for k in range(20):
  val_R = random.choice([2500,4000,3000,10000,19000,2999,7770,1231])
val_Ref.append([val_R])
for h in val_Ref:
  mycursor.execute(sql1,h)
mydb.commit()