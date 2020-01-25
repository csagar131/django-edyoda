import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sagar",
  passwd="11121991"
)

print(mydb)
