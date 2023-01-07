dict1 = {'Iran': [0,0,0,0,0] , 'Spain': [0,0,0,0,0] , 'Portugal' : [0,0,0,0,0] , 'Morocco': [0,0,0,0,0]}
iranlist = dict1['Iran']
spainlist = dict1['Spain']
porlist = dict1['Portugal']
morlist = dict1['Morocco']
# print(iranlist[0])

def num(string):
    global num1
    global num2
    num1 = int(string[0])
    num2 = int(string[-1])
for i in range(6):
    result = input()
    num(result)
    if i == 0:
        if num1 > num2:
            iranlist[0] +=1
            spainlist[1] +=1
        elif num1 == num2:
            iranlist[2] += 1
            spainlist[2] +=1
        else:
            iranlist[1] +=1
            spainlist[0] +=1
        iranlist[3] += num1 - num2
        spainlist[3] += num2 - num1
    elif i == 1:
        if num1 > num2:
            iranlist[0] +=1
            porlist[1] +=1
        elif num1 == num2:
            iranlist[2] += 1
            porlist[2] +=1
        else:
            iranlist[1] +=1
            porlist[0] +=1
        iranlist[3] += num1 - num2
        porlist[3] += num2 - num1
    elif i == 2:
        if num1 > num2:
            iranlist[0] +=1
            morlist[1] +=1
        elif num1 == num2:
            iranlist[2] += 1
            morlist[2] +=1
        else:
            iranlist[1] +=1
            morlist[0] +=1
        iranlist[3] += num1 - num2
        morlist[3] += num2 - num1
    elif i == 3:
        if num1 > num2:
            spainlist[0] +=1
            porlist[1] +=1
        elif num1 == num2:
            spainlist[2] += 1
            porlist[2] +=1
        else:
            spainlist[1] +=1
            porlist[0] +=1
        spainlist[3] += num1 - num2
        porlist[3] += num2 - num1
    elif i == 4:
        if num1 > num2:
            spainlist[0] +=1
            morlist[1] +=1
        elif num1 == num2:
            spainlist[2] += 1
            morlist[2] +=1
        else:
            spainlist[1] +=1
            morlist[0] +=1
        spainlist[3] += num1 - num2
        morlist[3] += num2 - num1
    else:
        if num1 > num2:
            porlist[0] +=1
            morlist[1] +=1
        elif num1 == num2:
            porlist[2] += 1
            morlist[2] +=1
        else:
            porlist[1] +=1
            morlist[0] +=1
        porlist[3] += num1 - num2
        morlist[3] += num2 - num1
        
        
        
    


iranlist[4] = iranlist[0]*3 + iranlist[2]
spainlist[4] = spainlist[0]*3 + spainlist[2]
porlist[4] = porlist[0]*3 + porlist[2]
morlist[4] = morlist[0]*3 + morlist[2]


dict1={k : v for k,v in sorted(dict1.items(),key=lambda item: (-int(item[1][4]) , -int(item[1][0]) , item[0]))} 
for key, value in dict1.items():
    print(key, 'wins:' , value [0] , ',', 'loses:' ,  value[1] , ',' , 'draws:' , value[2] , ',' , 'goal difference:' , value[3] ,',' , 'points:' ,value[4])
