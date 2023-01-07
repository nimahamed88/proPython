import mysql.connector

mydb = mysql.connector.connect(
  host="localhost" ,  # 'your_localhost' ,
  user="nima88" , #'your_username',
  password="", #'your_password' , 
  database="learn" # 'your_database'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM test ORDER BY height DESC, weight" # test is a database that contains information about employees ordered by height and weight.

mycursor.execute(sql)

myresult = mycursor.fetchall()

for (name , weight , height ) in myresult:
    print(name , height , weight) # first print height then weight
