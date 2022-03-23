d = {}
d["gg"] = 10
print(d["gg"])
for key, value in d.items():
    print("key")
    print(key)
    print("value")
    print(value)


# class and objects and constructors
class Register:
    def __init__(self, name, age, gender):  # this is a constructor and self is like this in java
        self.name = name
        self.age = age
        self.gender = gender

    def theFunction(self):
        print("this is their details" + " " + self.name + self.age + self.gender)


student = Register("jay", str(7), "male")  # to avoid concatenate error put the int in str brackets

student.theFunction()


# class Teacher:
#     def __init__(self, name, gender, number, is_sitting):
#         self.name = name
#         self.gender = gender
#         self.number = number
#         self.is_sitting = is_sitting
#
#     def sitDown(self):
#         self.is_sitting = False
#
#     def standUp(self):
#         self.is_sitting = True
#
#
# person = Teacher("lalay", "female", str(9), False)


# list comprehension
a= [1,2,3,4,5]
b=[]
for x in a:
    b.append(x*2) # [2, 4]
print(b)
for g in a:

#same

c= [x*2 for x in a] # it says d = is going to be a lis[ in which element of list is gonna x * 2 for each x in a
d = [x**2 for x in a]
d.reverse()
print(d)
range(10, 0, -1)# this describes range from 6 to 0 but will include zero thats why -1 is there
f =[]
for x  in range(6, 0 , -1):
    f.append(x**2)
print(f)
f2= [x**2 for x in range(6, 0 , -1)]
# set
g = set()
g.add(3)
#u cant add duplicates
#removing duplicates in list
given_list= [1,1,1,2,3,4,4]
new_set = set()
for x in given_list:
    new_set.add(x)
print (new_set)
#to get it back to a list
new_list=list()
for x in new_set:
    new_list.append(x)
print (new_list)
given_list2= [1,1,3,3,4]
new_set2= set()
for x in given_list2:
    new_set2.add(x)
total=0
for x in new_set2:
    total+=x
sum(new_set2)
print(total)

