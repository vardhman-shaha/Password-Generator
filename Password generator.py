import random
import string
 
def generate_password(length=8):
    """
    Function to generate a random password.
    
    Args:
        length (int): Length of the password to be generated. Default is 8.
    
    Returns:
        str: Generated password.
    """
    # Available character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # Special characters like !@#
    
    # Combine all character sets
    all_characters = letters + digits + symbols
    
    # Generate the password by randomly picking characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password
 
if __name__ == "__main__":
    # Ask user for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            raise ValueError("Password length should be at least 1")
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
 