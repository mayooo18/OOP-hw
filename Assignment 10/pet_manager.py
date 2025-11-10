from pet import Pet

def main ():

    name = input("Enter pet name: ")
    animal_type = input("Enter animal type: ")
    age = int(input("Enter pet age: "))

    my_pet = Pet(name, animal_type, age)

    print("Pet Information")
    print(f"Name: {my_pet.get_name()}")
    print(f"Animal Type: {my_pet.get_animal_type()}")
    print(f"Age: {my_pet.get_age()}")

if __name__ == "__main__":
    main()


