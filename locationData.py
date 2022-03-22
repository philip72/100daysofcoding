country = "Kenya"
county = "Nairobi"
city = "kilimani"
continent = "Africa"
print(county)

# swapping variables
temp = city
city = county
county = temp  # use the temporary variable to swp characters
print(county)

b = ["banana", "apple", "microsoft"]
tempr = b[0]
b[0] = b[2]
b[2] = tempr
print(b)
b[0], b[2] = b[2], b[0]
print(b)
for i in b:
    print(i)
    # for j in i:
    #     print (j)

total3 = 0
j = 1
while j < 100:
    total3 += j
    print(total3)
    j += 10
print(total3)

given_list = [5, 4, 4, 3, 1, -1, -2]
total4 = 0
l = 0
while l < len(given_list) and given_list[l] > 0:
    total4 += given_list[l]
    l += 1
print(total4)
for element in given_list:
    if element <= 0:
        break
    total4 += element
print(element)
total6 = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total6 += given_list[j]
    l -= 1
print(total4)


# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
#
#
# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → Tru

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
#
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3