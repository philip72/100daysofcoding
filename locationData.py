country = "Kenya"
county = "Nairobi"
city = "kilimani"
continent = "Africa"
print (county)

#swapping variables
temp = city
city= county
county= temp                #use the temporary variable to swp characters
print(county)

b = ["banana", "apple", "microsoft"]
tempr=b[0]
b[0]=b[2]
b[2]=tempr
print(b)
b[0], b[2]= b[2], b[0]
print(b)
for i in b:
    print(i)
    # for j in i:
    #     print (j)

total3= 0
j=1
while j< 100:
    total3 += j
    print(total3)
    j+=10
print(total3)

given_list = [5, 4, 4, 3, 1, -1, -2]
total4= 0
l= 0
while l < len(given_list ) and given_list[l]>0:
    total4 += given_list[l]
    l += 1
print(total4)
for element in given_list:
    if element <= 0:
        break
    total4 += element
print(element)
total6= 0
j = len(given_list)-1
while given_list[j] <0:
    total6+=given_list[j]
    l-=1
print(total4)