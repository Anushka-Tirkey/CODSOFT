import random
import string

l=int(input("Enter length of the password (>=6 and <=20)"))
if l>=6 and l<=20:
    def generate_password(length=l, use_uppercase=True, use_digits=True, use_special_chars=True):
        """
        Generate a random password.

        Parameters:
        - length: Length of the password (default is 12).
        - use_uppercase: Include uppercase letters in the password (default is True).
        - use_digits: Include digits in the password (default is True).
        - use_special_chars: Include special characters in the password (default is True).

        Returns:
        A randomly generated password.
        """
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    # Example usage:
    generated_password = generate_password()
    print("Generated Password:", generated_password)
else:
    print("Password cannot be generated for this length")