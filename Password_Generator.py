import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choices(all_chars, k=length))
    return password


try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid integer.")
