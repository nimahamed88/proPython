import random

class Human:

    def __init__(self):
        self.name = input().split('- ') # list of names
        self.name = list(map(str.strip, self.name)) #removing exta spaces in objects of list

        self.number = len(self.name)
        # print(self.number)
        # print(self.name) 



    def random(self):
        A = random.sample(self.name, self.number//2) # pick half of footbalists in teamA randomly
        # print(A)

        # B  = list(set(self.name) - set(A)) #creating list B
        # print(B)



        # for j in range(self.number//2):   # another way of creating list B
        #     for k in range(len(self.name)):
        #         if A[j] == self.name[k]:
        #             self.name.pop(k)
        #             print(self.name)
        #             break

        

        B = [i for i in self.name if i not in A]   #Another way of creating list B
        # print(B)

        for i in range(self.number//2):
            print (A[i], 'A')
        for l in range(self.number//2):
            print (B[l], 'B')
        
class Footbalist(Human):
    pass

a = Footbalist()
a.random()