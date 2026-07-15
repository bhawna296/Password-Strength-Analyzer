import secrets
import string

def generate_password(length=16):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password = []
    for _ in range(length):
        password.append(secrets.choice(all_characters))
        
    return ''.join(password)

