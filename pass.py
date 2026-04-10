import random
import string

def generate_password():
    print("\n===== PASSWORD GENERATOR =====")

    # Get length
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number")
        return

    if length <= 0:
        print("Length must be greater than 0")
        return

    # Choose pass
    print("\nSelect password type:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Symbols")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        characters = string.ascii_letters
    elif choice == '2':
        characters = string.ascii_letters + string.digits
    elif choice == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice")
        return

    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))

    print("\n Generated Password:", password)


# Run program
generate_password()