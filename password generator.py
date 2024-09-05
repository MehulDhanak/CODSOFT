# Python program for password generator

import random
import string

print("==== Welcome to Random Password Generator =====\n ")

length = int(input("Enter length of password: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

word = lower + upper + num + symbols

a = random.sample(word,length)
password = "".join(a)
print("Password is :",password)