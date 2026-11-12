
import random
import string

def generate_password():

    print("\n===== RANDOM PASSWORD GENERATOR =====")

    # Get password length
    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length >= 8:
                break
            else:
                print("Password length must be at least 8 characters.")

        except ValueError:
            print("Please enter a valid number.")

    # Character type selection
    print("\nSelect character types:")
    print("1. Uppercase Letters (A-Z)")
    print("2. Lowercase Letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$%^&*)")

    while True:
        choices = input("\nEnter your choices (e.g., 1234): ")

        if (choices.isdigit()
                and len(set(choices)) == len(choices)
                and all(c in "1234" for c in choices)
                and len(choices) >= 2):
            break

        print("Invalid selection! Choose at least 2 different types.")

    # Character pools
    character_sets = {
        "1": string.ascii_uppercase,
        "2": string.ascii_lowercase,
        "3": string.digits,
        "4": string.punctuation
    }

    # Combine selected character types
    characters = "".join(character_sets[c] for c in choices)

    # Ensure every selected type appears
    password = [
        random.choice(character_sets[c])
        for c in choices
    ]

    # Fill remaining password length
    password += [
        random.choice(characters)
        for _ in range(length - len(password))
    ]

    # Shuffle password characters
    random.shuffle(password)

    # Display password
    print("\nGenerated Password:", "".join(password))


# Main program
while True:

    generate_password()

    again = input("\nGenerate another password? (yes/no): ").lower()

    if again not in ["yes", "y"]:
        print("\nThank you for using Password Generator!")
        break
