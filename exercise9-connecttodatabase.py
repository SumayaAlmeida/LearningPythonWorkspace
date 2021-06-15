import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="csharp",
  password="password",
  database="hire"
)


mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM car")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

