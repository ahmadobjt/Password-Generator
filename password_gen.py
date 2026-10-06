# Password Generator

import random
import string

# Get password length from user
def get_password_length():
    '''Get a valid password length from the user.'''
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def user_choice():
    '''Get the character type selected by the user.'''
    print("Choose the type of characters to include in your password:")
    print("1. Lowercase letters")
    print("2. Uppercase letters")
    print("3. Numbers")
    print("4. Special characters")
    print("5. All of the above")

    while True:
        user_choice=input("Enter your choice (1-5): ").strip()
        try:
            raw=user_choice.replace(","," ").split()
            choices=[int(choice) for choice in raw]
            
            if choices and all(choice in range(1,6) for choice in choices):
                return set(choices)
            
            print("Choose num between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# create character pool
def create_character_pool(choices):
    '''Create a pool of character based on the user's choices.'''
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    nums=string.digits
    special_char=string.punctuation

    characters = ""
    if 1 in choices:
        characters += lowercase
    if 2 in choices:
        characters += uppercase
    if 3 in choices:
        characters += nums
    if 4 in choices:
        characters += special_char
    if 5 in choices:
        characters += special_char+uppercase+nums+lowercase
    return characters

# Generate password

def generate_password(length, characters):
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
     length=get_password_length()
     choices=user_choice()
     characters=create_character_pool(choices)
     password=generate_password(length,characters)
     
     print("Generated password: ",password)
     
if __name__=="__main__":
    main()