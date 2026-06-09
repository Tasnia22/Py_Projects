import random
import string

length = int(input("Enter the Length of the password: "))

char = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(char)

print("Generated Password:")
print(password)