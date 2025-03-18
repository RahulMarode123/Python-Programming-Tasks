import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
    
    if not char_pool:
        print("Error: No character types selected.")
        return None
    
    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Error: Password length must be greater than zero.")
            return
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Error: Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
