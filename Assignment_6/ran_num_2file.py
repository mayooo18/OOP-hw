import random

def main():
    #ask the user for a filename
    filename = input("Enter the filename to save  numbers: ")

    num = input("Enter how many random numbers you want to make: ")
    
    with open(filename, 'w') as file:
        for _ in range(int(num)):
            number = random.randint(1, 100)
            file.write(str(number) + "\n")
    print(f"{num} random numbers have been written to {filename}")



if __name__ == "__main__":
    main()