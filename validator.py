import re

def validate_password(password):
    """
    Business Rules:
    1. Length between 8 and 20 characters.
    2. Must contain at least one uppercase letter.
    3. Must contain at least one digit.
    4. Must contain at least one special character (@, #, $, %, !).
    """
    if not (8 <= len(password) <= 20):
        return False, "Length must be between 8 and 20 characters."
    
    if not re.search(r"[A-Z]", password):
        return False, "Missing uppercase letter."
        
    if not re.search(r"\d", password):
        return False, "Missing digit."
        
    if not re.search(r"[@#$%!]", password):
        return False, "Missing special character."
        
    return True, "Password is valid."

# Example Usage
if __name__ == "__main__":
    test_pwd = "Password123!"
    is_valid, message = validate_password(test_pwd)
    print(f"Testing '{test_pwd}': {message}")
'''
AI Integration: Ask students to use an LLM to "Refactor this function to be more
Pythonic using list comprehensions".
def validate_password_pythonic(password):
    special_chars = "@#$%!"

    if not (8 <= len(password) <= 20):
        return False, "Length must be between 8 and 20 characters."

    if not any(char.isupper() for char in password):
        return False, "Missing uppercase letter."

    if not any(char.isdigit() for char in password):
        return False, "Missing digit."

    if not any(char in special_chars for char in password):
        return False, "Missing special character."

    return True, "Password is valid."
    '''

