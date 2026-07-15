import re

COMMON_PASSWORDS = [
    "123456",   
    "password",
    "password123",
    "qwerty",
    "abc123",   
    "admin",
    "welcome",    
]

def check_password(password):
    score = 0
    suggestions = []    

    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        suggestions.append("Increase password length to at least 12 characters")
    else:
        suggestions.append("Password should be at least 8 characters long")

    if re.search(r'[a-z]', password):
        score += 15
    else:
        suggestions.append("Include at least one lowercase letter")    

    if re.search(r'[A-Z]', password):
        score += 15
    else:
        suggestions.append("Include at least one uppercase letter")

    if re.search(r'\d', password):
        score += 15
    else:   
        suggestions.append("Add at least one number")       
    

    if re.search(r'[^A-Za-z0-9]', password):
        score += 15
    else:
        suggestions.append("Include at least one special character")

    if password.lower() in COMMON_PASSWORDS:
        score -= 10
        suggestions.append("Avoid using common passwords")     

    return score, suggestions

import math

def entropy(password):
    """Estimate the Shannon entropy (bits) of the password based on used character sets."""

    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32 

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)

