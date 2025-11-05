import pickle
import os

DATA_FILE = 'email.dat'

def load_emails():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'rb') as f:
        return pickle.load(f)
    
def save_emails(email_dict):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(email_dict, f)

def email_lokup(email_dict):
    email = input("Enter the email address to look up: ")
    if email in email_dict:
        print(f"The name associated with {email} is {email_dict[email]}.")
    else:
        print(f"No entry found for {email}.")

def add_email(email_dict):
    email = input("Enter the email address to add: ")
    if email in email_dict:
        print(f"{email} already exists with name {email_dict[email]}.")
        return
    
    note = input("Enter the name or note related with this email: ")

    email_dict[email] = note

    save_emails(email_dict)
    print(f"Added {email} with note '{note}'.")

def lookup_email(data):
    email = input("Enter email to look up: ")
    if email in data:
        print(f"{email} → {data[email]}")
    else:
        print("Email not found.")

def add_email(data):
    email = input("Enter new email: ")
    if email in data:
        print("That email already exists.")
        return
    note = input("Enter name or note for this email: ")
    data[email] = note
    save_emails(data)
    print("Email added and saved.")

def modify_email(data):
    email = input("Enter the email to modify: ").strip()
    if email not in data:
        print("Email not found.")
        return
    print(f"Current value: {data[email]}")
    new_value = input("Enter new name/note: ").strip()
    data[email] = new_value
    save_emails(data)
    print("Email updated and saved.")

def delete_email(data):
    email = input("Enter the email to delete: ").strip()
    if email not in data:
        print("Email not found.")
        return
    confirm = input(f"Are you sure you want to delete {email}? (y/n): ").lower().strip()
    if confirm == "y":
        del data[email]
        save_emails(data)
        print("Email deleted and saved.")
    else:
        print("Deletion canceled.")

def main():
    data = load_emails()
    print("Loaded", len(data), "emails.")

    while True:
        print("\n=== Email Menu ===")
        print("[1]Lookup  [2]Add  [3]Modify  [4]Delete  [5]Quit")
        choice = input("Choose an option: ").lower().strip()

        if choice == "1":
            lookup_email(data)
        elif choice == "2":
            add_email(data)
        elif choice == "3":
            modify_email(data)
        elif choice == "4":
            delete_email(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if main() == "__main__":
    main()
