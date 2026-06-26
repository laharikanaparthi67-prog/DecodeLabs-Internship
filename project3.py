print("=== Password Confirmation System ===")

password_length = 8

password = input("Create a password (8 characters): ")

if len(password) == password_length:
    confirm_password = input("Confirm your password: ")

    if password == confirm_password:
        print("Password created successfully!")
        print("Password Length:", password_length)
    else:
        print("Passwords do not match!")
else:
    print("Password must be exactly", password_length, "characters long.")