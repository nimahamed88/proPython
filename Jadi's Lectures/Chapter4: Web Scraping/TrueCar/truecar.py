import re
import requests
import mysql.connector
from bs4 import BeautifulSoup

#request from site:
model = input('Enter your car model: ')
r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/{0}/'.format(model)) # which car model?



#connect to my Database:
mydb = mysql.connector.connect(
  user='nima88',
  password='',
  host='127.0.0.1',
  database = 'learn' #my Database
)

mycursor = mydb.cursor()

#create table in my Database

TableName = '{0}_table'.format(model)
# print(TableName)

mycursor.execute('CREATE TABLE %s (name varchar(30),price varchar(30),age varchar(30))' % TableName)


counter = 0
soup = BeautifulSoup(r.text , 'html.parser')
articles = soup.find_all('div' , attrs={
  'class': ['card-content',
  'order-3',
  'vehicle-card-body']})

for article in articles:
    counter += 1
    if counter == 21:  #first 20 cars
        break
    else:
        names = article.find('span' , attrs={'class' : 'truncate'})
        names = names.text #name of car
        
        prices = article.find('div', attrs={'class': ['heading-3' , 'my-1' , 'font-bold']})
        prices = prices.text #price of the car
        
        works = article.find('div' , attrs={'data-test' : 'vehicleMileage'})
        works = works.text #mile age of the car
        
        
        # print(names)
        # print(prices)  
        # print(works) 

        # print('------')



        #INSERT VALUES TO TABLE

        Sql = 'INSERT INTO {0} (name , price , age) VALUES (%s, %s , %s )'.format(TableName)
        vals = (names , prices , works)
        # print(vals)
        mycursor.execute(Sql, vals)



# print(counter)

mydb.commit()

#read from table:


# reader = "SELECT * FROM {0}".format(TableName)

# mycursor.execute(reader)

# myresult = mycursor.fetchall()

# for (name , price , age ) in myresult:
#     print(name,'|' , price, '|', age)

mydb.close
  
