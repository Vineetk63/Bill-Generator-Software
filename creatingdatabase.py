import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vin#@0786",
)
c=mydb.cursor()

c.execute("CREATE DATABASE shop")

--vineet
