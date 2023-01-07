from datetime import date

def calculate_age(born):
    today = str(date.today()).split('-')
    today = list(map(int,today)) 
    born = list(map(int,born))
    year = today[0] - born[0] - (today[1] < born[1])
    if born[1] > 12:
        print('WRONG')
    elif born[2] > 31:
        print('WRONG')
    else:
        print(year)

age = input().split('/')
calculate_age(age)