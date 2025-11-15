import bcrypt
import os
USER_DATA_FILE = "users.txt" #defining the user data file
#implement the Password Hashing Function
def hash_password(plain_text_password):
    bytes_password = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes_password, salt)
    return hashed_password
#impliment password verification function
def verify_password(plain_text_password, hashed_password):
    bytes_plain_text_password = plain_text_password.encode('utf-8')
    return bcrypt.checkpw(bytes_plain_text_password, hashed_password)
test_password = "SecurePassword123"
# Test hashing
hashed = hash_password(test_password)
print(f"Original password: {test_password}")
print(f"Hashed password: {hashed}")
print(f"Hash length: {len(hashed)} characters")
# Test verification with correct password
is_valid = verify_password(test_password, hashed)
print(f"\nVerification with correct password: {is_valid}")
# Test verification with incorrect password
is_invalid = verify_password("WrongPassword", hashed)
print(f"Verification with incorrect password: {is_invalid}")


# implementing user registration
username= "Eunice"
password = "JUL187"
def register_user(username, password):
    hashed_pass = hash_password(password)
    with open ("users.txt", "a") as f:
        f.write(f'{username};{hashed_pass}\n')
    return True
print(f"user '{username}' registered")

#USER EXISTENCE CHECK
def user_exists(username):
    with open("users.txt", "r") as f:
        for line in f:
            if line.strip() == username:
                return True  # Username found

    return False  # Username not found


# implementing user login
def login_user(username, password):
    with open ("users.txt", "a") as f:
        for line in f.readlines():
            user, hash=line.strip().split(":")
            if user == username:
                return verify_password(password, hash)
    return False

# implement input validation
def validate_username(username):
    # This function will later check if the username is valid.
    # 'pass' is a placeholder meaning "do nothing yet"
    pass

def validate_password(password):
    # This function will later check if the password is valid.
    # 'pass' is a placeholder meaning "do nothing yet"
    pass

#impliment main menu


def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)


def main():
    """Main program loop."""
    # Displays a welcome message when the program starts
    print("\nWelcome to the Week 7 Authentication System!")

    # Starts an infinite loop so the menu keeps showing until user chooses Exit
    while True:
        # Display the main menu
        display_menu()
        # Ask the user for their choice (1–3)
        choice = input("\nPlease select an option (1-3): ").strip()


        # Option 1: Register a new user

        if choice == '1':
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Validate username using the function (will return True/False + message)
            is_valid, error_msg = validate_username(username)

            # If the username is not valid, print the error message and go back to the menu
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Ask user for a password
            password = input("Enter a password: ").strip()

            # Validate the password (you’ll define this function later)
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Ask user to confirm the password
            password_confirm = input("Confirm password: ").strip()

            # Check if the two passwords match
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # If everything is valid, register the user (you’ll define this function later)
            register_user(username, password)


        # Option 2: Login

        elif choice == '2':
            print("\n--- USER LOGIN ---")

            # Ask for login credentials
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt to log in (you’ll define this function later)
            if login_user(username, password):
                print("\nYou are now logged in.")
                print("(In a real application, you would now access the data)")

            # Wait for user to press Enter before returning to main menu
            input("\nPress Enter to return to main menu...")


        # Option 3: Exit

        elif choice == '3':
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break  # Breaks the loop to end the program


        # Invalid Option: an option that isn't in the menu
        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")


# This ensures the main() function only runs when this file is executed directly
if __name__ == "__main__":
    main()

#__name__ known for dunder name or double underscore name is a special variable that Python automatically creates for every module (file)...