

def validate_password(pw: str) -> list:
    errors =[]

    if len(pw) < 8 :
        errors.append("Password must be at least 8 characters long.")
    
    if not any(ch.isupper() for ch in pw) or not any(ch.islower() for ch in pw) or not any(ch.isdigit() for ch in pw):
        errors.append("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")

    if not pw.isalnum():
        errors.append("Password must not contain special characters.")

    return errors
    

def main():
    password = input("Enter a password: ")

    validation_errors = validate_password(password)

    if validation_errors:
        for e in validation_errors:
            print(e)
        print("Password is invalid.")

    else:
        print("Password is valid.")


if __name__ == "__main__":
    main()
