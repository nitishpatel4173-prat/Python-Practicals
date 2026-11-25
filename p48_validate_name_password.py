# Practical 48: Validate name (alphabets only) and password (must contain a digit)

name = input("Enter name (alphabets only): ").strip()
password = input("Enter password (must include a digit): ")

name_valid = name.isalpha()                                # letters only, not empty
password_valid = any(char.isdigit() for char in password)  # at least one digit

if name_valid and password_valid:
    print("Validation successful. Registration complete.")
else:
    if not name_valid:
        print("Invalid name: use alphabets only (no digits, spaces or symbols).")
    if not password_valid:
        print("Invalid password: it must include at least one digit.")
