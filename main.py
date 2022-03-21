# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# for loop
c = list(range(1, 9))
total = 0
for i in c:
    total = total + i
    print(total)

# sum of multiples of 3, 5 that are less than are hundred
totall = 0
for i in range(0, 100):
    if i % 3 == 0:
        totall += i
    elif i % 5 == 0:
        totall += i

print(totall)


def c_greater_than_d_plus_e(f, d, e):
    if f > d+e:
        return True
    else:
        return False


c_greater_than_d_plus_e(2, 3, 5)
