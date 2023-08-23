import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vin#@0786",
    database="shop"
)
c=mydb.cursor()
c.execute("CREATE TABLE customer(name varchar(20),number varchar(15),email varchar(30),totalbill integer,bill_num integer)")