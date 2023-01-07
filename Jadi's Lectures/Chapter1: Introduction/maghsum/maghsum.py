def maghsum(x):
    m = 0
    for q in range(1,x+1):
        if x % q == 0:
            m+=1
    return m
max1 = 0
maxn = []
for i in range(10):
    num = int(input())
    answer = maghsum(num)
    if answer > max1:
        maxn = []
        max1 = answer
        maxn.append(num)
    elif answer == max1:
        maxn.append(num)
    else:
        continue
print(max(maxn) , max1)