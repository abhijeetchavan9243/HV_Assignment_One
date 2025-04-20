import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    # Uppercase and lowercase check
    if not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")
        return False

    # Digit check
    if not re.search(r'\d', password):
        print("Password must contain at least one digit.")
        return False

    # Special character check
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
        return False

    return True

# Main script
if __name__ == "__main__":
    user_password = input("Enter your password to check its strength: ")
    if check_password_strength(user_password):
        print("Your password is strong!")
    else:
        print("Your password is weak. Please try again.")