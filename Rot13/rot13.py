#!/usr/bin/python3


alphabet = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(text):
    text = text.lower()
    result = 'Your Output is : '    
    for char in text:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) + 13) % 26]
        else:
            result += char
    return result

def decrypt(text):
    text = text.lower()
    result = 'Your Output is : '    
    for char in text:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) - 13) % 26]
        else:
            result += char
    return result

user_option = input("Enter Option: \n1. ROT13 Encryption\n2. ROT13 Decryption\n\nYour choice :")
if (user_option == "1"):
    user_input = input("Enter the text: ")
    print(encrypt(user_input))
    
elif (user_option == "2"):
    user_input = input("Enter the text: ")
    print(decrypt(user_input))
else:
    print("Enter correct option")
