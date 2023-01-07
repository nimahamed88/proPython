import statistics
class mad1:
    age_list = []
    height_list = []
    weight_list = []
    def __init__(self , age , height , weight ):
        self.age = age
        self.height = height 
        self.weight = weight
    def get_age(self):
        self.age = (input())
        mad1.age_list = self.age.split()
        mad1.age_list = list(map(int , mad1.age_list))
        # print( mad1.age_list)
    def get_height(self):
        self.height = (input())
        mad1.height_list = self.height.split()
        mad1.height_list = list(map(int , mad1.height_list))
        # print( mad1.height_list)
    def get_weight(self):
        self.weight = (input())
        mad1.weight_list = self.weight.split()
        mad1.weight_list = list(map(int , mad1.weight_list))
        # print( mad1.weight_list)
    def return_info(self):
        print(mad1.age_list , mad1.height_list , mad1.weight_list)

    def return_mean(self):
        print(statistics.fmean(mad1.age_list))
        print(statistics.fmean(mad1.height_list))
        print(statistics.fmean(mad1.weight_list))



class mad2:
    age_list = []
    height_list = []
    weight_list = []
    def __init__(self , age , height , weight ):
        self.age = age
        self.height = height 
        self.weight = weight
    def get_age(self):
        self.age = (input())
        mad2.age_list = self.age.split()
        mad2.age_list = list(map(int , mad2.age_list))
        # print( mad1.age_list)
    def get_height(self):
        self.height = (input())
        mad2.height_list = self.height.split()
        mad2.height_list = list(map(int , mad2.height_list))
        # print( mad1.height_list)
    def get_weight(self):
        self.weight = (input())
        mad2.weight_list = self.weight.split()
        mad2.weight_list = list(map(int , mad2.weight_list))
        # print( mad1.weight_list)
    def return_info(self):
        print(mad2.age_list , mad2.height_list , mad2.weight_list)

    def return_mean(self):
        print(statistics.fmean(mad2.age_list))
        print(statistics.fmean(mad2.height_list))
        print(statistics.fmean(mad2.weight_list))


numberA = int(input())


person1 = mad1(mad1.get_age , mad1.get_height , mad1.get_weight)
person1.get_age()
person1.get_height()
person1.get_weight()


numberB = int(input())


person2 = mad2(mad2.get_age , mad2.get_height , mad2.get_weight)
person2.get_age()
person2.get_height()
person2.get_weight()


person1.return_mean()
person2.return_mean()

if statistics.fmean(mad1.height_list) > statistics.fmean(mad2.height_list):
    print('A')
elif statistics.fmean(mad1.height_list) < statistics.fmean(mad2.height_list):
    print('B')
else:
    if statistics.fmean(mad1.weight_list) > statistics.fmean(mad2.weight_list):
        print('B')
    elif statistics.fmean(mad1.weight_list) <  statistics.fmean(mad2.weight_list):
        print('A')
    else:
        print('Same')
