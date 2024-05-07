import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="world"
)

mycursor = mydb.cursor()
rsp = mycursor.execute("SELECT * FROM city where CountryCode = 'IDN'")
myresult = mycursor.fetchall()
for x in myresult:
    print(x[1])