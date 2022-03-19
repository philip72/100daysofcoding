# weight = int(input("enter your weight"))
# height = int(input("enter your height in meters "))
#
# bmi = weight / (height ** 2)
# print(bmi)
# if bmi < 25:
#     print("you are okay")
# elif bmi ==25:
#     print("need to work out abit")
# else:
#     print("you are overweight")

def bmi_calc(weight, height):
    weight=int(input('enter your weight'))
    height=int(input('enter your height'))
    bmi = weight / (height**2)
    print(bmi)


bmi_calc(weight=0, height= 0)
