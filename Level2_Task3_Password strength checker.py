import re

def password_checker(password):
    
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False
    
    if not re.search(r'[!@#$%^&*]', password):
        return False

    return True



password = input("Enter your password: ")


if password_checker(password):
    print("Password is strong.")
else:
    print("Password is not strong. Please follow the password factors.")
    
    
    
    
