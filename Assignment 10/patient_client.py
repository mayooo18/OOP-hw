from patient import Patient
from procedure import Procedure

def main():
    print("Enter Patient Information:")
    firstname = input("First Name: ")
    lastname = input("Last Name: ")
    address = input("Address: ")
    phone = input("Phone Number: ")
    emergency_contact = input("Emergency Contact: ")

    patient = Patient(firstname, lastname, address, phone, emergency_contact)

    print("\nEnter Procedure Information:")

    procedures = []

    while True:
        name = input("Procedure Name: ")
        date = input("Procedure Date (MM/DD/YYYY): ")
        practitioner = input("Practitioner Name: ")
        charge = float(input("Procedure Charge: $"))

        procedure = Procedure(name, date, practitioner, charge)
        procedures.append(procedure)

        more = input("Add another procedure? (yes/no): ")

        if more.lower() != 'yes':
            break
    
    print("patient info:")
    print(patient)

    print("procedures")

    for p in procedures:
        print(p)
       

if __name__ == "__main__":
    main()