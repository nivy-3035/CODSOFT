import random
import string
def password(length, use_uppercase, use_digits, use_special):
    char = string.ascii_lowercase
    if uppercase:
        char += string.ascii_uppercase
    if digits:
        char += string.digits
    if special:
        char += string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password
def main():
 print("Welcome to the Password Generator!")
while True:
    try:
            length = int(input("Enter the desired length of the password: "))
    finally:
        length <= 0
        break
print("Please enter a valid positive integer for the password length")
uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
digits = input("Include digits? (yes/no): ").lower() == 'yes'
special = input("Include special characters? (yes/no): ").lower() == 'yes'
password = password(length,uppercase,digits,special)
print(f"\nPassword: {password}")

