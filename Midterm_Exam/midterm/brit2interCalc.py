#function that shows the options
def menuoptions():
    print("1. Convert Pounds to Kilograms")
    print("2. Convert Ounce to Grams")
    print("3. Convert inches to Centimeters")
    print("0. Exit")



#function that processes the request and uses try except for value errors
def loopformenu():
    active = True
    while active == True:
        menuoptions()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("invalid choice only enter number (0-3)")
            continue

        if choice == 1:
            try:
                pounds = float(input("Enter weight in Pounds: "))
                kilograms = pounds * 0.453592
                print(f"{pounds} Pounds is equal to {kilograms:.2f} Kilograms\n")
            except ValueError:
                print("Enter Valid Number")



        elif choice == 2:
            try:
                ounces = float(input("Enter weight in Ounces: "))
                grams = ounces * 28.3495
                print(f"{ounces} Ounces is equal to {grams:.2f} Grams\n")
            except ValueError:
                print("Enter Valid Number")

        
        elif choice == 3:
            try:
                inches = float(input("Enter length in Inches: "))
                centimeters = inches * 2.54
                print(f"{inches} Inches is equal to {centimeters:.2f} Centimeters\n")
            except ValueError:
                print("Enter Valid Number")

        
        elif choice == 0:
            active = False
            print("Exiting the program.")
        

        else:
            print("Invalid choice. Please try again.")
    

#function that applies all of the above.
#  if i were to expand on it i would make them into classes and just leave the main here 

def main():
    loopformenu()
    


if __name__ == "__main__":
    main()
    
        



