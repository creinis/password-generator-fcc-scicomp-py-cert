# Password Generator

import re
import secrets
import string

def generate_password(length=20, nums=1, special_chars=1, uppercase=1, lowercase=1):
    
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_characters = letters + digits + symbols
    
    while True:
        password = ''
        
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        

    
    return password