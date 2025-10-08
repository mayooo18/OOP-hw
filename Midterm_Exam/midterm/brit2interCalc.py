def menuoptions():
    print("1. Convert Pounds to Kilograms")
    print("2. Convert Ounce to Grams")
    print("3. Convert inches to Centimeters")
    print("0. Exit")




def loopformenu():
    active = True
    while active == True:
        menuoptions()

        choice = int(input("Enter your choice: "))
        if choice == 1:
            pounds = float(input("Enter weight in Pounds: "))
            kilograms = pounds * 0.453592
            print(f"{pounds} Pounds is equal to {kilograms:.2f} Kilograms\n")
        elif choice == 2:
            ounces = float(input("Enter weight in Ounces: "))
            grams = ounces * 28.3495
            print(f"{ounces} Ounces is equal to {grams:.2f} Grams\n")
        elif choice == 3:
            inches = float(input("Enter length in Inches: "))
            centimeters = inches * 2.54
            print(f"{inches} Inches is equal to {centimeters:.2f} Centimeters\n")
        
        elif choice == 0:
            active = False
            print("Exiting the program.")
        

        else:
            print("Invalid choice. Please try again.")
     
def main():
    loopformenu()
    


if __name__ == "__main__":
    main()
    
        



