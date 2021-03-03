import string
import random

name1 = string.ascii_lowercase
name2 = string.ascii_uppercase
name3 = string.digits
name4 = string.punctuation

#ask the user for the password length
passwordLength = int(input("Enter password lenght: "))

#make a list of characters
list_of_char = []
list_of_char.extend(name1)
list_of_char.extend(name2)
list_of_char.extend(name3)
list_of_char.extend(name4)

#create a string to get random character of given length.
final_password = "".join(random.sample(list_of_char, passwordLength))
print("Your password is: "+final_password)
