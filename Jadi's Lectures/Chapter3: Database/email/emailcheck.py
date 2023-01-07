import mysql.connector
import re

#connect to your database

mydb = mysql.connector.connect(
  host="localhost",
  user="nima88",
  password="",
  database="learn"
)

mycursor = mydb.cursor()

 
# Make a regular expression
# for validating an Email

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a function for
# for validating an Email

def check(email, item):
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        item += 1
        return email , item
 
    else:
        print("Invalid Email! Use valid format like: expression@string.string")
        email = input('Enter your email again please: ')
        return email , item


sql = "INSERT INTO email (username, password) VALUES (%s, %s)" #email is a table.

email = input('Enter your email: ') # Enter your email here

count = 0
while count == 0:
    val3 = check(email,count)
    count = val3[1]
    email = val3[0]

value = (email, input('Enter your password: '))
mycursor.execute(sql, value)

mydb.commit()
mydb.close()
