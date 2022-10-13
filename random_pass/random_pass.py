from string import ascii_letters, digits
from random import choice

collection = ascii_letters + digits
password = ""
l = int(input("Length of password needed to be generated: "))
for i in range(l):
    password += choice(collection)
print("Random Generated Password: ", password)
