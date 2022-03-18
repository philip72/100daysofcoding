import random
import math

alphabets = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
special_characters = "!@#$%^&*()_+?:"

# password length takes the rule of 50-30-20

# ask for user input i.e. the password length they want
password_length = int(input("enter your desires password length "))

# enhance by use of countdown thus generate a password length of 8
alphabets_length = password_length //2
numbers_length = math.ceil(password_length * 30 / 100)
special_characters_length = password_length - (alphabets_length + numbers_length)

password = []


def generate_password(length, array, is_alphabet=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alphabet:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)


# alphabet password
generate_password(alphabets_length, alphabets, True)
# numeric password
generate_password(numbers_length, numbers)
# special characters
generate_password(special_characters_length, special_characters)

random.shuffle(password)

gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)
