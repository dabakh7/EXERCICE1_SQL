import mysql.connector 
import random

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Dabakh7.",
  database = "Exercice_BDD"
)
mycursor = mydb.cursor()
sql = "INSERT INTO VEHICULES (modele,Marque,Annee) VALUES ( %s, %s, %s)"
val_veh=[]
for k in range(30):
  val_m = random.choice (['Renauld','Toyota','Mercedes','BMW'])
  val_mod = random.choice(['auris','aygo','bz4x','austral','Arkana'])
  val_d = random.choice([2021,2018,2010,2014,2004,2000])
    #choice ne prend qu'un seul élément
  val_veh.append([val_mod,val_m,val_d]) #Il faut respecter l'ordre donné en haut

for i in val_veh: 
  mycursor.execute(sql,i)
  # mycursor.execute(sql,(10,'renauld Clio','Renauld',1990))

mydb.commit()