

###################


# در این برنامه ابتدا از ۱۰ صفحه اول سایت
#truecar.com
#اطلاعاتی راجع به مدل ماشین مورد نظر مانند سال تولید، کارکرد و قیمت آن را استخراج کرده و وارد دیتابیس و جدول مورد نظر میکنیم
# سپس با استفاده از الگوریتم درخت داده ها را از جدول خارج کرده و با سال تولید و کارکرد ماشین خود فیت کرده و الگوریتم، قیمت پیش بینی
# شده برای ماشین ما را به ما برمیگرداند
 


###################

import re
import requests
import mysql.connector
from bs4 import BeautifulSoup
from sklearn import tree


#request from site:
model = input('Enter your car model: ').casefold()
#connect to my Database:
mydb = mysql.connector.connect(
  user='nima88',
  password='',
  host='127.0.0.1',
  database = 'learn' #my Database
)

mycursor = mydb.cursor()

#create table in my Database

TableName = '{0}_MLTable'.format(model)
# print(TableName)
mycursor.execute('DROP TABLE IF EXISTS %s' % TableName)
mycursor.execute('CREATE TABLE %s (name varchar(35) , year int ,age_miles int , price varchar(10))' % TableName)
counter = 0

for i in range(10): #look data for 10 pages 
  r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/{0}/?page={1}'.format(model,i+1)) # which car model?






  soup = BeautifulSoup(r.text , 'html.parser')
  articles = soup.find_all('div' , attrs={
    'class': ['card-content',
    'order-3',
    'vehicle-card-body']})

  for article in articles:
      counter +=1

      names = article.find('span' , attrs={'class' : 'truncate'})
      names = names.text #name of car
      
    

      prices = article.find('div', attrs={'data-test': 'vehicleListingPriceAmount'})
      prices = prices.text #price of the car
      
      works = article.find('div' , attrs={'data-test' : 'vehicleMileage'})
      works = works.text #mile age of the car
      works = re.sub(r'miles' , '' , works).strip()
      works = re.sub(r',' , '' , works)
      works = int(works)
      
      
      years = article.find('span' , attrs={'class' : 'vehicle-card-year'})
      years = int(years.text) # year of the car
      # print(names)
      # print(prices)  
      
      # print(works) 
      # print(years)
      # print('------')



      #INSERT VALUES TO TABLE

      Sql = 'INSERT INTO {0} (name , year , age_miles , price) VALUES (%s, %s , %s , %s )'.format(TableName)
      vals = (names , years , works , prices)
      # print(vals)
      mycursor.execute(Sql, vals)


# print(type(names))
# print(type(prices))
# print(type(works))
# print(type(years))

# print(counter)
mycursor.execute('ALTER TABLE {0} ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'.format(TableName))
mydb.commit()



#######################

#DATABASE CREATED!

#######################

# read from database_table:

# reader = "SELECT * FROM {0}".format(TableName)

# mycursor.execute(reader)
 
# myresult = mycursor.fetchall()



# for (name , year , age , price , id) in myresult:

#     print( year, '|', age , '|' , price )

  


##################

# ML process starts:

##################


reader = "SELECT * FROM {0}".format(TableName)

mycursor.execute(reader)
 
myresult = mycursor.fetchall()

x =[]
y=[]

count = 0
for ( name ,year , age , price , id ) in myresult:
  count +=1
  x.append([year, age])
  y.append(price)
  
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

new_data = [[int(input('Enter your car year: ')) ,int(input('Enter your car MileAge: ')) ]]
answer = clf.predict(new_data)

print('Prediction of your \'{0}\' car price is: '.format(model) , answer[0])

mydb.close()

