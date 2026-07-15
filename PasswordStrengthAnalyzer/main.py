from password_checker import check_password, entropy
from password_generator import generate_password
from database import *

create_database()

password = input("Enter Password: ")    

if password_exists(password):
    print("\nThis password has already been used.")
else:
    score, suggestions = check_password(password)
    entropy_value = entropy(password)

    print("\nPassword Score:", score)
    print("\nPassword Entropy:", entropy_value, "bits")

    if score >= 85:
        print("Strength: Very Strong")
    elif score >= 65:
        print("Strength: Strong")
    elif score >= 45:
        print("Strength: Medium")
    else:
        print("Strength: Weak")

    print("\nSuggestions:")

    if suggestions:
        for item in suggestions:
            print("-", item)
    else:
        print("Excellent Password")

    print("\nSuggested Strong Password")

    print(generate_password())

    save_password(password)