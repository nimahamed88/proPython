n = int(input())
d = dict()
for i in range(n):
    text = input().split() # text to list (4 items)
    for j in range(3):
        d[text[j+1]] = text[0]
#dictionary done
sent = input().split() # sentence to a list
result = ''
for i in range(len(sent)):
    if sent[i] in d:
        result += d[sent[i]] + ' '
    else:
        result += sent[i] + ' '
print(result)