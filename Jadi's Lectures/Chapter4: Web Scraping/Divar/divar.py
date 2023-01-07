import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://divar.ir/s/tehran') # صفحه اول دیوار برای شهر تهران:
# r.text

soup = BeautifulSoup(r.text , 'html.parser')
articles = soup.find_all('article' , attrs={
  'class': ['kt-post-card',
  'kt-post-card--outlined',
  'kt-post-card--padded',
  'kt-post-card--has-action']})
num = articles.__len__()

# print(articles.__len__()) # تعداد آگهی های قابل رویت
i = 0
for article in articles:
    # print(article.text)
    # name = BeautifulSoup(article.text , 'html.parser')
    name = article.find('h2' , attrs={'class': 'kt-post-card__title'})
    price = article.find('div', attrs={'class': "kt-post-card__description"})
    date = article.find('span' , attrs= { 'class': "kt-post-card__bottom-description kt-text-truncate"}) 
    if price == None:
      pass
    else:
      # print(price.text)
      if ('توافقی' in price.text):
        print('نام آگهی: ' , name.text , '|' , 'قیمت: ' , price.text , '|' ,  'مکان و زمان: ' , date.text)
        i+=1

if i == 0:
    print(' هیچ آگهی با تگ قیمت توافقی از مجموعِ {0} آگهی پیدا نشد!'.format(num))

