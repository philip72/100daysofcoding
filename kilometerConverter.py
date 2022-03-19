# kilometers=float(input("enter what u want to convert to miles"))
# kilometersToMiles=0.621371
# miles=kilometersToMiles*kilometersToMiles
# print('%0.2f kilometres is equal to %0.2f miles'%(kilometers,miles))
#
def km_convert(miles):
    kilomet =  float(input('write kilom'))
    miles= '{:.2f}'.format(0.621371*kilomet)
    print(miles)


km_convert(miles=0)